#!/usr/bin/env python3
"""ContentSphere sample AWS CDK application."""

import os

import aws_cdk as cdk
from aws_cdk import (
    Stack,
    CfnOutput,
    CfnParameter,
    aws_ec2 as ec2,
)
from constructs import Construct


class ContentSphereStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        project_name = "ContentSphere"

        allowed_ssh_cidr = CfnParameter(
            self,
            "AllowedSshCidr",
            type="String",
            default="127.0.0.1/32",
            description="Trusted public IP in CIDR notation, for example x.x.x.x/32",
        )

        vpc = ec2.Vpc(
            self,
            "ContentSphereVpc",
            ip_addresses=ec2.IpAddresses.cidr("10.30.0.0/16"),
            max_azs=2,
            nat_gateways=0,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="Public",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24,
                )
            ],
        )

        web_security_group = ec2.SecurityGroup(
            self,
            "ContentSphereWebSecurityGroup",
            vpc=vpc,
            description="HTTP access and restricted SSH for ContentSphere",
            allow_all_outbound=True,
        )

        web_security_group.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(80),
            "Allow public HTTP",
        )

        web_security_group.add_ingress_rule(
            ec2.Peer.ipv4(allowed_ssh_cidr.value_as_string),
            ec2.Port.tcp(22),
            "Allow SSH from the configured trusted IP",
        )

        user_data = ec2.UserData.for_linux()
        user_data.add_commands(
            "dnf install -y httpd",
            "systemctl enable --now httpd",
            "cat > /var/www/html/index.html <<'HTML'",
            "<!doctype html>",
            "<html><head><title>ContentSphere</title></head>",
            "<body><h1>ContentSphere</h1>",
            "<p>Infrastructure Provisioned using AWS CDK</p></body></html>",
            "HTML",
        )

        web_server = ec2.Instance(
            self,
            "ContentSphereWebServer",
            instance_type=ec2.InstanceType("t3.micro"),
            machine_image=ec2.MachineImage.latest_amazon_linux2023(),
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            ),
            security_group=web_security_group,
            user_data=user_data,
            require_imdsv2=True,
        )

        cdk.Tags.of(self).add("Project", project_name)
        cdk.Tags.of(self).add("Environment", "dev")
        cdk.Tags.of(self).add("ManagedBy", "AWS-CDK")

        CfnOutput(
            self,
            "VpcId",
            value=vpc.vpc_id,
            description="ContentSphere VPC ID",
        )

        CfnOutput(
            self,
            "WebServerInstanceId",
            value=web_server.instance_id,
            description="ContentSphere EC2 instance ID",
        )

        CfnOutput(
            self,
            "WebsiteUrl",
            value=f"http://{web_server.instance_public_dns_name}",
            description="ContentSphere website URL",
        )


app = cdk.App()

ContentSphereStack(
    app,
    "ContentSphereCdkStack",
    env=cdk.Environment(
        account=os.environ.get("CDK_DEFAULT_ACCOUNT"),
        region=os.environ.get("CDK_DEFAULT_REGION", "ap-south-1"),
    ),
)

app.synth()
