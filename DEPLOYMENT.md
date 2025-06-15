# Deployment Guide

This guide covers different methods to deploy the Health Perks API with HTTPS support.

## Option 1: Using Nginx as a Reverse Proxy (Recommended)

1. Install Nginx:
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install nginx

# CentOS/RHEL
sudo yum install nginx
```

2. Install Certbot for SSL certificates:
```bash
# Ubuntu/Debian
sudo apt install certbot python3-certbot-nginx

# CentOS/RHEL
sudo yum install certbot python3-certbot-nginx
```

3. Create Nginx configuration:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

4. Obtain SSL certificate:
```bash
sudo certbot --nginx -d your-domain.com
```

5. Run the FastAPI application:
```bash
# Install gunicorn
pip install gunicorn

# Run with gunicorn
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000
```

## Option 2: Using Docker with Traefik

1. Create a Dockerfile:
```dockerfile
FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

2. Create docker-compose.yml:
```yaml
version: '3'

services:
  api:
    build: .
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.api.rule=Host(`your-domain.com`)"
      - "traefik.http.routers.api.entrypoints=websecure"
      - "traefik.http.routers.api.tls=true"
      - "traefik.http.routers.api.tls.certresolver=myresolver"

  traefik:
    image: traefik:v2.5
    command:
      - "--api.insecure=true"
      - "--providers.docker=true"
      - "--providers.docker.exposedbydefault=false"
      - "--entrypoints.websecure.address=:443"
      - "--certificatesresolvers.myresolver.acme.tlschallenge=true"
      - "--certificatesresolvers.myresolver.acme.email=your-email@example.com"
      - "--certificatesresolvers.myresolver.acme.storage=/letsencrypt/acme.json"
    ports:
      - "443:443"
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock:ro"
      - "./letsencrypt:/letsencrypt"
```

3. Deploy:
```bash
docker-compose up -d
```

## Option 3: Using Cloud Platforms

### AWS Elastic Beanstalk

1. Install EB CLI:
```bash
pip install awsebcli
```

2. Initialize EB application:
```bash
eb init
```

3. Create environment:
```bash
eb create production
```

4. Configure HTTPS in AWS Console or using AWS CLI

### Google Cloud Run

1. Install Google Cloud SDK

2. Build and push container:
```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/health-perks-api
```

3. Deploy to Cloud Run:
```bash
gcloud run deploy health-perks-api \
  --image gcr.io/YOUR_PROJECT_ID/health-perks-api \
  --platform managed \
  --allow-unauthenticated
```

## Environment Variables

Set these environment variables in your production environment:

```bash
SECRET_KEY=your-secure-secret-key
DATABASE_URL=your-production-database-url
BACKEND_CORS_ORIGINS=["https://your-frontend-domain.com"]
```

## Security Considerations

1. Always use HTTPS in production
2. Set secure headers:
   - HSTS
   - X-Content-Type-Options
   - X-Frame-Options
   - Content-Security-Policy

3. Use secure session management
4. Implement rate limiting
5. Regular security updates
6. Monitor application logs
7. Backup database regularly

## Monitoring

1. Set up logging:
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
```

2. Consider using monitoring tools:
   - Prometheus + Grafana
   - New Relic
   - Datadog
   - AWS CloudWatch 