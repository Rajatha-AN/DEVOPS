# Exercise 2 – Deploy Flask Application on Kubernetes

## Objective

Deploy a simple Flask application as a Docker container and run it on a local Kubernetes cluster using Minikube.

## Technologies Used

- Python
- Flask
- Docker
- Kubernetes
- Minikube
- kubectl

## 1. Create Flask Application

Created a simple Flask application using `app.py`.

The application returns:

```text
Hello from Flask on Kubernetes!

Run the application on port 15000.

2. Create Docker Image

Created a Dockerfile to containerize the Flask application.

Built the Docker image using:

docker build -t flask-app .

Verified the image using:

docker images
3. Load Image into Minikube

Loaded the locally created Docker image into the Minikube cluster:

minikube image load flask-app:latest
4. Create Kubernetes Deployment

Created flask-deployment.yaml to deploy the Flask application.

Applied the deployment using:

kubectl apply -f flask-deployment.yaml

Verified the deployment using:

kubectl get deployments
5. Verify the Pod

Checked the running pods using:

kubectl get pods

The Flask pod reached the Running state.

6. Expose the Application

Exposed the deployment using a NodePort service:

kubectl expose deployment flask-deployment --type=NodePort --port=15000 --target-port=15000

Verified the service using:

kubectl get services
7. Access the Application

Opened the Flask application using:

minikube service flask-deployment

The application was successfully accessed in the browser and displayed:

Hello from Flask on Kubernetes!

Result

The Flask application was successfully containerized using Docker, deployed to Kubernetes using Minikube, exposed through a NodePort service, and accessed successfully through a web browser.

