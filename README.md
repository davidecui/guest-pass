# GuestPass

GuestPass is a simple, local-first web application that generates printable WiFi access cards with QR codes for your guests. The whole project is based on the following youtube video, with some additional features and modifications, but still using Antigravity for development.

https://www.youtube.com/watch?v=ooHyVrYY_2U

## Features

- **Instant QR Code Generation**: Enter your WiFi credentials efficiently.
- **Privacy Focused**: Runs entirely locally; no data leaves your network.
- **Printable Cards**: Generates a clean, card-sized layout for printing.
- **Standard Security**: Supports WPA/WPA2 authentication methods.

## Getting Started

### Prerequisites

- Python 3.8+
- [Optional] Docker

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd guest-pass
   ```

2. **Set up a virtual environment**
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r app/requirements.txt
   ```

### Usage

Run the application:

```bash
python app/main.py
```

Open your browser and navigate to:
[http://127.0.0.1:8000](http://127.0.0.1:8000)

### Docker Support

To run using Docker:

1. Navigate to the app directory:
   ```bash
   cd app
   ```

2. Build and run the container:
   ```bash
   docker build -t guest-pass .
   docker run -p 8000:8000 guest-pass
   ```

## Deploying to GCP

### Prerequisites

Before running the Terraform configuration, enable the following APIs on your GCP project:

```bash
gcloud services enable run.googleapis.com
gcloud services enable artifactregistry.googleapis.com
```

Or enable them via the GCP Console:
- [Cloud Run Admin API](https://console.cloud.google.com/apis/library/run.googleapis.com)
- [Artifact Registry API](https://console.cloud.google.com/apis/library/artifactregistry.googleapis.com)

### Required IAM Roles

The service account used by Terraform / GitHub Actions needs the following roles:

| Role | Purpose |
|---|---|
| `roles/run.admin` | Create and manage Cloud Run services |
| `roles/artifactregistry.writer` | Push Docker images |
| `roles/iam.serviceAccountUser` | Act as the Compute Engine default SA used by Cloud Run |

Grant them with:

```bash
export SA_EMAIL="YOUR_TERRAFORM_SA@YOUR_PROJECT.iam.gserviceaccount.com"
export PROJECT_ID="YOUR_PROJECT_ID"

gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SA_EMAIL" \
  --role="roles/run.admin"

gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SA_EMAIL" \
  --role="roles/artifactregistry.writer"

# Grant actAs on the Compute Engine default service account used by Cloud Run
gcloud iam service-accounts add-iam-policy-binding \
  $(gcloud projects describe $PROJECT_ID --format='value(projectNumber)')-compute@developer.gserviceaccount.com \
  --member="serviceAccount:$SA_EMAIL" \
  --role="roles/iam.serviceAccountUser" \
  --project=$PROJECT_ID
```

> **Note**: The last command fixes the `Permission 'iam.serviceaccounts.actAs' denied` error that occurs when Terraform creates the Cloud Run service.

### Deploying

```bash
cd terraform
terraform init
terraform apply -var="project_id=YOUR_PROJECT_ID"
```


## License


[MIT](LICENSE)
