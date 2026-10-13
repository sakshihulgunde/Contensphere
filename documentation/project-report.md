# ContentSphere – Infrastructure as Code Deployment and Automation using Terraform

## 1. Project Information

- Student Name: Sakshi Hulgunde
- Batch Code: DRA-501
- Project Title: ContentSphere – Infrastructure as Code Deployment and Automation using Terraform
- Cloud Platform: Amazon Web Services (AWS)
- Infrastructure as Code Tool: Terraform
- AWS Region: Asia Pacific (Mumbai) – ap-south-1
- Environment: Development

## 2. Introduction

ContentSphere is an Infrastructure as Code (IaC) project that demonstrates
how cloud infrastructure can be defined and managed through configuration
files rather than relying entirely on manual configuration in the AWS console.

Terraform is used to organize infrastructure into reusable modules. This
approach improves consistency, maintainability, and the ability to review
infrastructure changes through version control.

## 3. Objectives

- Define AWS infrastructure using Terraform.
- Organize infrastructure into reusable modules.
- Configure networking, security, compute, and storage components.
- Deploy a sample web server using EC2 user data.
- Apply security best practices to network access and S3 storage.
- Use Git and GitHub for source control.
- Configure a GitHub Actions workflow for Terraform formatting and validation.

## 4. Technologies Used

- Amazon Web Services (AWS)
- Terraform
- Amazon VPC and networking components
- Amazon EC2
- Amazon S3
- Linux command line
- Git and GitHub
- GitHub Actions
- CloudFormation and AWS CDK as additional infrastructure templates

## 5. Proposed Architecture

The Terraform configuration is designed to create the following infrastructure:

1. A Virtual Private Cloud (VPC) for network isolation.
2. A public subnet for the web server.
3. An Internet Gateway and route table for internet routing.
4. A security group that permits HTTP traffic and restricts SSH access according
   to the configured source CIDR.
5. An EC2 instance running Amazon Linux with user data to install and configure
   an Apache web server.
6. An S3 bucket configured with encryption, versioning, and public-access
   blocking.

The Terraform root configuration calls separate modules for networking,
security, compute, and storage.

## 6. Terraform Module Structure

- modules/vpc: Defines the VPC, public subnet, Internet Gateway, route table,
  and route association.
- modules/security-group: Defines inbound HTTP and restricted SSH rules,
  together with outbound rules.
- modules/ec2: Defines the Amazon Linux EC2 instance and web server
  initialization.
- modules/s3: Defines the S3 bucket, encryption, versioning, and
  public-access-block settings.

The root configuration uses input variables and module outputs to make the
configuration easier to maintain and reuse.

## 7. Implementation Details

The project uses Terraform configuration files to describe the desired
infrastructure. Variables control settings such as AWS region, project name,
environment, network CIDRs, EC2 instance type, and permitted SSH source CIDR.

The EC2 module uses user data to install Apache and create a sample
ContentSphere web page when the instance initializes.

The S3 module enables versioning and server-side encryption and blocks public
access to reduce the risk of accidental data exposure.

The repository also includes a CloudFormation template and an AWS CDK
application as additional infrastructure-as-code examples. These are separate
implementations and have not been confirmed as deployed.

## 8. Version Control and Automation

Git is used to track project changes, while GitHub can be used to store and
share the source code.

A GitHub Actions workflow is included to check Terraform formatting,
initialize Terraform without configuring a remote backend, and validate the
configuration.

The presence of the workflow file does not by itself confirm that a GitHub
Actions run has succeeded. Workflow execution should be checked in the GitHub
repository before reporting it as completed.

## 9. Validation and Testing

The following local checks have been completed:

- Terraform formatting check: passed.
- Terraform configuration validation: passed.
- Git whitespace check: passed after cleaning README trailing whitespace.
- CloudFormation YAML parsing and basic structure check: passed.

Local Terraform validation confirms that Terraform can parse and validate the
configuration. The local CloudFormation check confirms YAML parsing and
basic structure only.

AWS-side CloudFormation validation, successful provisioning, website
accessibility, and live infrastructure behavior have not been confirmed.

## 10. Security Considerations

- Do not commit AWS access keys, secret keys, or other credentials.
- Keep terraform.tfvars and Terraform state files out of version control.
- Prefer an IAM role with least-privilege permissions over long-lived access
  keys.
- Restrict SSH access to a trusted public IP address.
- Keep S3 public-access blocking enabled.
- Enable encryption and versioning for the S3 bucket.
- Review Terraform plans before applying changes.
- Check potential AWS charges before creating or retaining resources.
- Verify credentials are secure before performing any AWS operations.

## 11. Current Deployment Status

Local Terraform formatting and validation have passed. The CloudFormation
template has passed a local YAML syntax and basic structure check.

Actual AWS resource provisioning and website verification have not been
confirmed. Remote Terraform state and Elastic IP deployment are not confirmed
as implemented or tested and should not be reported as completed without
evidence.

The project should be considered locally validated, not a verified live AWS
deployment.

## 12. Future Enhancements

- Verify deployment in a secured AWS environment.
- Configure remote Terraform state with appropriate access controls and
  state locking support.
- Add monitoring, logging, and alerting.
- Improve automated testing and deployment workflows.
- Add cost monitoring and resource cleanup procedures.

## 13. Conclusion

ContentSphere demonstrates a modular approach to Infrastructure as Code using
Terraform. It organizes networking, security, compute, and storage into
reusable modules and includes source-control automation and additional
infrastructure templates.

The local configuration checks have passed. Further secured AWS validation
and deployment testing are required before the infrastructure can be
described as successfully deployed and operational.
