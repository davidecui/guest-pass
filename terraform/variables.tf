variable "project_id" {
  description = "The Google Cloud Project ID"
  type        = string
}

variable "region" {
  description = "The application region"
  type        = string
  default     = "us-central1"
}

variable "service_name" {
  description = "The name of the Cloud Run service"
  type        = string
  default     = "guest-pass"
}

variable "repository_name" {
  description = "The name of the Artifact Registry repository"
  type        = string
  default     = "guest-pass-repo"
}
