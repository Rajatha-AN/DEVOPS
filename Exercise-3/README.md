# Exercise 3 – Scaling Flask App on Single Node using ReplicaSets

## Objective

Deploy a Flask-based Flash Sale application on Minikube using Kubernetes ReplicaSets.

The application is designed to demonstrate:

- Running multiple replicas of a Flask application
- Scaling replicas from 3 to 5
- Self-healing when a pod is deleted
- Running all replicas on a single Minikube node
- Accessing the application through a Kubernetes Service
- Observing which pod serves each request

---

## Application

The Flask application provides three endpoints:

### `/`

Returns a welcome message, pod hostname, and timestamp.

Example response:

```json
{
  "message": "Welcome to Big Sale!",
  "pod": "flashsale-rs-n9wjm",
  "ts": 1758896940.123
}
/buy

Simulates a purchase during a flash sale.

Example:

/buy?user=123

The response contains:

Purchase status
Randomly selected product
User ID
Pod that served the request
Request time

Example response:

{
  "item": "Smartphone",
  "served_by_pod": "flashsale-rs-rqxbr",
  "status": "success",
  "time": "14:29:59",
  "user": "123"
}
/health

Used by Kubernetes readiness and liveness probes to check application health.

Example response:

{
  "status": "healthy",
  "pod": "flashsale-rs-xxxxx"
}
Technologies Used
Python
Flask
Gunicorn
Docker
Kubernetes
Minikube
kubectl
Kubernetes ReplicaSet
Kubernetes ClusterIP Service
Project Structure
Exercise-3/
├── ex3-flash-sale.py
├── Dockerfile
├── flashsale-replicaset.yaml
├── README.md
└── exercise-3-flash-sale-output.png
Step 1 – Start Minikube

Start Minikube using Docker:

minikube start --driver=docker

Verify the cluster:

kubectl get nodes
Step 2 – Use Minikube Docker Environment

Configure the terminal to use Minikube's Docker environment:

eval $(minikube docker-env)
Step 3 – Build the Docker Image

Build the Flash Sale application image:

DOCKER_BUILDKIT=0 docker build -t flashsale:1.0 .

Verify the image:

docker images

The image should contain:

flashsale   1.0
Step 4 – Deploy the ReplicaSet

Apply the Kubernetes configuration:

kubectl apply -f flashsale-replicaset.yaml

The ReplicaSet initially creates 3 pods.

Verify:

kubectl get rs

Expected result:

NAME          DESIRED   CURRENT   READY
flashsale-rs  3         3         3

Verify the pods:

kubectl get pods

Three Flash Sale pods should be running.

Step 5 – Scale the ReplicaSet

Scale the application from 3 replicas to 5 replicas:

kubectl scale rs flashsale-rs --replicas=5

Verify:

kubectl get rs

Expected result:

NAME          DESIRED   CURRENT   READY
flashsale-rs  5         5         5

Verify the pods:

kubectl get pods

Five pods should be running.

Step 6 – Test Self-Healing

Delete one of the running Flash Sale pods:

kubectl delete pod <pod-name>

For example:

kubectl delete pod flashsale-rs-fmxwm

Then verify:

kubectl get pods

Kubernetes automatically creates a replacement pod to maintain the desired replica count of 5.

Verify the ReplicaSet:

kubectl get rs

Expected result:

NAME          DESIRED   CURRENT   READY
flashsale-rs  5         5         5

This demonstrates the self-healing behavior of a Kubernetes ReplicaSet.

Step 7 – Verify All Pods Run on a Single Node

Run:

kubectl get pods -o wide

All five pods are scheduled on the Minikube node:

minikube

This demonstrates scaling multiple application replicas on a single Kubernetes node.

Step 8 – Access the Application

The application is exposed internally using a ClusterIP Service named:

flashsale-svc

Get the Service URL:

minikube service flashsale-svc --url

Open the generated URL in a browser.

Step 9 – Test the Flash Sale Application

Open:

/buy?user=123

The application returns the pod that handled the request.

Example:

{
  "item": "Smartphone",
  "served_by_pod": "flashsale-rs-rqxbr",
  "status": "success",
  "time": "14:29:59",
  "user": "123"
}

Refreshing the request can result in another replica serving the request, demonstrating Service-based traffic distribution across the pods.

Kubernetes Configuration

The flashsale-replicaset.yaml file contains:

ReplicaSet with 3 initial replicas
Flash Sale application container
Container port 5000
Readiness probe
Liveness probe
CPU and memory resource requests/limits
ClusterIP Service
Service port 80 mapped to container port 5000
Health Checks

The application uses the /health endpoint for Kubernetes probes.

Readiness Probe
readinessProbe:
  httpGet:
    path: /health
    port: 5000
Liveness Probe
livenessProbe:
  httpGet:
    path: /health
    port: 5000

These probes allow Kubernetes to check whether the application is ready to receive traffic and whether it is still running correctly.
Results

The exercise successfully demonstrated:

Flask application containerization using Docker.
Deployment of the application on Minikube.
Running 3 initial replicas using a ReplicaSet.
Scaling the ReplicaSet from 3 to 5 replicas.
Maintaining 5 replicas after deleting a pod.
Automatic creation of a replacement pod.
Running all replicas on the single Minikube node.
Accessing the application through a Kubernetes Service.
Identifying which pod served a request using the /buy endpoint.
