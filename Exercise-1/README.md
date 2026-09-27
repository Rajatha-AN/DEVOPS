# Exercise 1 – Kubernetes Getting Started

## Objective

Deploy an Nginx container as a Pod using Kubernetes and Minikube, expose it using a NodePort Service, and access the application through a web browser.

## Environment

- Operating System: macOS
- Container Runtime: Docker Desktop
- Kubernetes: Minikube
- Application: Nginx

## Steps Performed

### 1. Start Minikube

Started a local Kubernetes cluster using Minikube with Docker as the driver.

bash
minikube start --driver=docker


### 2. Create an Nginx Pod

Created a Pod named `hello-k8s` using the Nginx image.

```bash
kubectl run hello-k8s --image=nginx --port=80
```

### 3. Verify the Pod

Checked the status of the Pod using:

```bash
kubectl get pods
```

The Pod successfully reached the `Running` state.

### 4. Expose the Pod

Exposed the Pod using a NodePort Service on port 80.

```bash
kubectl expose pod hello-k8s --type=NodePort --port=80
```

### 5. Access the Application

Opened the Nginx application using:

```bash
minikube service hello-k8s
```

The Nginx welcome page was successfully displayed in the browser.


