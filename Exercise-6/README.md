# Exercise 6 – Jenkins CI/CD with Prometheus and Grafana

## Objective

To implement a Jenkins-based CI/CD pipeline for a Dockerized application and monitor the application using Prometheus and Grafana.

## Technologies Used

- Jenkins
- Docker
- Python
- Flask
- Prometheus
- Grafana
- Git / GitHub
- Ubuntu Linux

## Project Files

- `delivery_metrics.py` – Python application exposing Prometheus metrics
- `Dockerfile` – Docker image for the metrics application
- `Dockerfile.jenkins` – Custom Jenkins Docker image with Docker CLI
- `Jenkinsfile` – Jenkins CI/CD pipeline
- `prometheus.yml` – Prometheus configuration
- `alert_rules.yml` – Prometheus alert rules
- `.gitignore` – Excludes virtual environment and Python cache files

## Jenkins Pipeline

The Jenkins pipeline performs the following stages:

1. **Pre-check Docker** – Verifies Docker availability.
2. **Setup Workspace** – Checks the Exercise 6 files.
3. **Build Docker Image** – Builds the `delivery_metrics` Docker image.
4. **Run Application** – Runs the application on port `8000`.
5. **Run Prometheus & Grafana** – Creates and starts Prometheus and Grafana containers.
6. **Verify Services** – Displays the running containers and service URLs.

## Services

| Service | Port | URL |
|---|---:|---|
| Delivery Metrics | 8000 | http://localhost:8000/metrics |
| Prometheus | 9090 | http://localhost:9090 |
| Grafana | 3000 | http://localhost:3000 |
| Jenkins | 8080 | http://localhost:8080 |

## Result

The Jenkins pipeline was successfully executed and completed with **Finished: SUCCESS**.

The following Docker containers were verified as running:

- `delivery_metrics`
- `prometheus`
- `grafana`
- `jenkins`

## Conclusion

The exercise demonstrates a basic CI/CD workflow using Jenkins with Docker, along with application monitoring using Prometheus and Grafana.
