# Terraform Remote State
terraform {
  backend "s3" {
    bucket = "custom-emr-state-bucket"
    key    = "key/terraform.tfstate"
    region = "eu-central-1"
  }
}
