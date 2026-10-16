terraform {
  required_version = ">= 1.7"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }

  backend "s3" {
    # Fill in or override via -backend-config
    bucket         = "REPLACE_WITH_STATE_BUCKET"
    key            = "REPLACE_WITH_STATE_KEY/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-state-lock"
    encrypt        = true
  }
}

provider "aws" {
  region = var.region

  default_tags {
    tags = {
      env        = var.environment
      managed-by = "terraform"
      prefix     = var.prefix
    }
  }
}
