module "vpc" {
  source             = "./modules/vpc"
  project_name       = var.project_name
  vpc_cidr           = var.vpc_cidr
  public_subnet_cidr = var.public_subnet_cidr
}

module "security_group" {
  source           = "./modules/security-group"
  project_name     = var.project_name
  vpc_id           = module.vpc.vpc_id
  allowed_ssh_cidr = var.allowed_ssh_cidr
}

module "ec2" {
  source            = "./modules/ec2"
  project_name      = var.project_name
  instance_type     = var.instance_type
  subnet_id         = module.vpc.public_subnet_id
  security_group_id = module.security_group.security_group_id
}

module "s3" {
  source       = "./modules/s3"
  project_name = var.project_name
}
