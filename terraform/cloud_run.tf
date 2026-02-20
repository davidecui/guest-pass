resource "google_cloud_run_v2_service" "dev" {
  name     = "${var.service_name}-dev"
  location = var.region
  ingress  = "INGRESS_TRAFFIC_ALL"

  template {
    containers {
      image = "us-docker.pkg.dev/cloudrun/container/hello:latest"
      ports {
        container_port = 8000
      }
    }
  }
}

resource "google_cloud_run_v2_service" "prod" {
  name     = var.service_name
  location = var.region
  ingress  = "INGRESS_TRAFFIC_ALL"

  template {
    containers {
      image = "us-docker.pkg.dev/cloudrun/container/hello:latest"
      ports {
        container_port = 8000
      }
    }
  }
}
