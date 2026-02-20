terraform {
  required_version = ">= 1.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }

  backend "gcs" {
    # Configured via CLI flags:
    # terraform init -backend-config="bucket=YOUR_BUCKET_NAME"
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}
