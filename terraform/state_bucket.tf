resource "google_storage_bucket" "terraform_state" {
  name          = "${var.project_id}-tfstate"
  location      = var.region
  force_destroy = false

  versioning {
    enabled = true
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      num_newer_versions = 5
    }
  }
}
