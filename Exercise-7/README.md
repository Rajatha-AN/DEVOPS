# Exercise 7 – Introduction to Continuous Integration (CI) and Jenkins Installation

## Objective

To understand the fundamentals of Continuous Integration (CI), learn the key concepts of Jenkins, and install and access Jenkins using Docker.

---

## What is Continuous Integration (CI)?

Continuous Integration (CI) is a development practice where developers frequently integrate their code changes into a shared repository. The primary goal is to detect and address errors early in the development process, improving software quality and accelerating delivery.

---

## Key Features of CI

1. **Frequent Code Integration**
   - Developers commit code to a shared repository multiple times a day.

2. **Automated Builds**
   - Every commit can trigger an automated build to verify the code changes.

3. **Automated Testing**
   - Automated tests can run as part of the CI process to ensure functionality remains intact.

4. **Immediate Feedback**
   - Developers receive quick feedback on their changes, allowing them to address issues promptly.

---

## Benefits of CI

- **Early Bug Detection** – CI helps identify integration issues early.
- **Improved Collaboration** – Developers work together on the same codebase.
- **Faster Development Cycles** – Automated builds and tests speed up development.
- **High-Quality Code** – Continuous testing helps prevent regressions.

---

## How CI Works

1. **Developer Workflow**
   - Developers write code and push changes to a version control system such as Git.

2. **CI Server Workflow**
   - The CI server detects code changes and triggers the build process.

3. **Automated Build**
   - The codebase is built and required dependencies are resolved.

4. **Automated Testing**
   - Unit tests, integration tests, and other automated tests are executed.

5. **Feedback**
   - Build and test results are communicated back to developers.

---

## Examples of CI Tools

### 1. GitLab CI/CD

GitLab CI/CD provides CI/CD capabilities integrated directly with Git repositories.

### 2. CircleCI

CircleCI is a cloud-based CI/CD platform known for integration with GitHub and Bitbucket.

### 3. Travis CI

Travis CI is a CI service commonly used for open-source and private projects.

### 4. Bamboo

Bamboo is an Atlassian CI/CD tool that integrates with Jira and Bitbucket.

### 5. TeamCity

TeamCity is a CI/CD server from JetBrains with support for multiple platforms and integrations.

### 6. Azure DevOps

Azure DevOps provides CI/CD pipelines with integration with Azure and Visual Studio.

### 7. GitHub Actions

GitHub Actions provides CI/CD automation directly within GitHub repositories.

### 8. Spinnaker

Spinnaker is an open-source continuous delivery platform for cloud-native applications.

### 9. Buildkite

Buildkite is a hybrid CI/CD platform that supports scalable and containerized workflows.

### 10. Drone

Drone is a modern CI/CD platform using a lightweight, containerized approach.

---

## CI Workflow Example

A basic CI workflow consists of:

1. **Code Change** – A developer pushes code to a Git repository.
2. **Trigger Build** – The CI server detects the change and triggers a build.
3. **Run Tests** – Automated tests validate the code.
4. **Feedback** – Developers receive the build and test results.

---

# Introduction to Jenkins

## What is Jenkins?

Jenkins is an open-source automation server used to build, test, and deploy software. It helps automate software development processes related to Continuous Integration (CI) and Continuous Delivery (CD).

---

## Why Use Jenkins?

- **Automation** – Automates repetitive development tasks.
- **Continuous Integration** – Helps integrate code changes smoothly.
- **Extensibility** – Supports plugins for different tools and services.
- **Scalability** – Can run builds on multiple machines.

---

## Key Jenkins Concepts

1. **Job/Project**
   - A task or process that Jenkins runs.

2. **Build**
   - The process of compiling and packaging code.

3. **Pipeline**
   - A series of steps used to build, test, and deploy an application.

4. **Plugins**
   - Extensions that add functionality to Jenkins.

5. **Nodes**
   - Machines where Jenkins runs jobs.

---

# Getting Started with Jenkins

## 1. Install Jenkins Using Docker

Jenkins can be installed using Docker with the following command:

```bash
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts
Port Configuration
8080 – Jenkins web interface
50000 – Jenkins agent communication

Note: In this practical exercise, the Jenkins instance that was already configured during the previous Docker-based exercise was reused instead of creating a second Jenkins container, because the container name jenkins and ports 8080 and 50000 were already in use.

2. Check Jenkins Container

The Jenkins container was verified using:

sudo docker ps -a --filter name=jenkins

The Jenkins container was found to be running with ports:

0.0.0.0:8080->8080/tcp
0.0.0.0:50000->50000/tcp
3. Access Jenkins on Port 8080

Jenkins was accessed through:

http://localhost:8080/

The Jenkins dashboard was successfully displayed.

Jenkins Dashboard

The Jenkins dashboard provides access to:

New Item
Build History
Build Queue
Manage Jenkins
Jenkins Jobs/Projects

The existing Exercise-6-Pipeline job was visible on the Jenkins dashboard.

Result

Jenkins was successfully installed and accessed using Docker.

The Jenkins dashboard was available on port 8080, confirming that Jenkins was running successfully and was ready to execute CI/CD jobs.
