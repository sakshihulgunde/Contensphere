# ContentSphere – Infrastructure as Code Deployment and Automation using Terraform

**Student:** Sakshi Hulgunde
**Batch:** DRA-501
**Environment:** Development
**AWS Region:** Asia Pacific (Mumbai) — `ap-south-1`

## Project Overview

ContentSphere is an Infrastructure as Code (IaC) learning project that uses Terraform to define reusable AWS infrastructure components. The objective is to make infrastructure configuration organized, repeatable, maintainable, and version-controlled.

This repository is a customized learning project based on the [AWS Terraform Starter](https://github.com/egezamb/aws-terraform-starter). The original repository is credited as the starting point.

## Objectives

- Define AWS infrastructure using Terraform.
- Organize infrastructure into reusable modules.
- Manage configuration through input variables and outputs.
- Apply security practices to networking and storage.
- Use GitHub for source control.
- Automate Terraform formatting and validation using GitHub Actions.

## Architecture

The intended architecture includes:

- **VPC:** Isolated virtual network.
- **Public subnet:** Subnet for the web server.
- **Internet Gateway and route table:** Internet routing.
- **Security group:** Controls permitted inbound and outbound traffic.
- **EC2:** Amazon Linux web server running Apache.
- **S3:** Storage bucket with versioning, encryption, and public-access blocking.

## Terraform Modules

| Module | Purpose |
|---|---|
| `modules/vpc` | VPC, subnet, Internet Gateway, and routing |
| `modules/security-group` | EC2 network security rules |
| `modules/ec2` | EC2 instance and web-server configuration |
| `modules/s3` | S3 bucket security and configuration |

The root `main.tf` connects these modules. `variables.tf` defines input settings, and `outputs.tf` exposes selected resource attributes.

## Repository Structure

```text
.
├── .github/workflows/terraform.yml
├── main.tf
├── variables.tf
├── outputs.tf
├── providers.tf
├── terraform.tfvars.example
├── modules/
│   ├── vpc/
│   ├── security-group/
│   ├── ec2/
│   └── s3/
├── documentation/
│   └── project-report.md
├── screenshots/
├── cloudformation/
├── cdk/
└── README.md
```

## Prerequisites

- Terraform CLI
- AWS CLI
- An AWS account with appropriately scoped permissions, if deploying
- Git

## Validate the Configuration

Run these commands from the project root:

```bash
terraform init
terraform fmt -recursive
terraform validate
terraform plan
```

Review the plan and potential costs before deployment. Successful validation does not mean AWS resources have been created.

## Configuration and Security

Copy `terraform.tfvars.example` to `terraform.tfvars` and update the values for your environment.

- Never commit AWS credentials, secrets, or Terraform state.
- Restrict SSH access to a trusted IP address.
- Keep S3 public-access blocking enabled.
- Review resource costs before deployment.
- Prefer temporary credentials or an appropriately scoped IAM role.
- Review the Terraform plan before applying changes.

## CI/CD

The GitHub Actions workflow checks Terraform formatting, initializes the configuration without a remote backend, and validates the Terraform files.

## Project Status

The modular Terraform configuration has been initialized and validated locally. Actual AWS provisioning, website reachability, Elastic IP configuration, and remote state must be verified separately before being reported as completed.

**Project message:** Infrastructure Provisioned using Terraform

## License and Attribution

The repository started from [egezamb/aws-terraform-starter](https://github.com/egezamb/aws-terraform-starter). Refer to the included LICENSE file and upstream repository for licensing terms.
