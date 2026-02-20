output "dev_service_url" {
  value = google_cloud_run_v2_service.dev.uri
}

output "prod_service_url" {
  value = google_cloud_run_v2_service.prod.uri
}
