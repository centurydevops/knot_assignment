# knot_assignment


---

##  `README.md`

```markdown
# Knot Infrastructure Assignment

## Overview
This project simulates investigating intermittent 5xx errors in a web application deployed on AWS using Terraform and Docker.

---

## Infrastructure Setup

### Prerequisites
- AWS account
- Terraform installed
- Docker installed
- EC2 key pair created
- GitHub Container Registry access

---

### Steps

1. **Clone the Repo**  
   ```bash
   git clone [https://github.com/YOUR_USERNAME/knot-assignment](https://github.com/centurydevops/knot_assignment.git)
   cd knot-assignment
## Buid and push image to ECR or Any repo
cd app
docker build -t knot-http-server .
docker tag knot-http-server ghcr.io/YOUR_USERNAME/knot-http-server:latest
docker push ghcr.io/YOUR_USERNAME/knot-http-server:latest

## Provision infrastructure
cd terraform
terraform init
terraform fmt
terraform validate
terraform plan
terraform apply -auto-approve


## Access Application

Visit: http://<EC2_PUBLIC_IP>/

~20% of the time, the server will return a 500 Internal Server Error.
