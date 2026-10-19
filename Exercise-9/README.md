# Exercise 9 – Jenkins Multi-Stage Pipeline: Deploying a Python Application

## Objective

To create and execute a Jenkins Pipeline that performs multiple stages for a sample Python Flask application.

The pipeline demonstrates:

- Build
- Test
- Deploy
- Run Application
- Test Application

---

## Project Structure

```text
Exercise-9/
├── .gitignore
├── Jenkinsfile
├── README.md
└── python-flask-app/
    ├── app.py
    ├── requirements.txt
    └── test_app.py

The Python virtual environment is excluded from Git using .gitignore.

1. Python Flask Application

The application is created in python-flask-app/app.py.

The application provides the following response at /:

Hello, Jenkins Multi-Stage Pipeline!
requirements.txt
flask==2.1.2
Unit Test

test_app.py uses Python's unittest framework to test the Flask application's / endpoint.

The test verifies:

HTTP status code is 200
Response is Hello, Jenkins Multi-Stage Pipeline!

The application was tested locally using:

python3 -m unittest discover -s .

The test completed successfully.

2. Jenkins Pipeline

A declarative Jenkins Pipeline was created in Jenkinsfile.

The pipeline contains the following stages:

Build

Installs the Python application dependencies using:

python3 -m pip install -r requirements.txt
Test

Runs the unit tests using:

python3 -m unittest discover -s .
Deploy

Creates a mock deployment directory and copies app.py into it:

mkdir -p ${WORKSPACE}/python-app-deploy
cp ${WORKSPACE}/python-flask-app/app.py ${WORKSPACE}/python-app-deploy/
Run Application

Runs the deployed Flask application in the background and stores its process ID.

Test Application

Runs the application test again after deployment.

3. Jenkins Configuration

Jenkins is already installed and running from the previous exercises.

Jenkins is accessed at:

http://localhost:8080

A new Jenkins Pipeline job will be created with a name such as:

Python-MultiStage-Pipeline

Under Pipeline configuration:

Definition: Pipeline script from SCM
SCM: Git
Repository:
https://github.com/Rajatha-AN/DEVOPS.git
Branch:
*/main

The Jenkinsfile is located at:

Exercise-9/Jenkinsfile
4. Pipeline Flow
GitHub Repository
       ↓
Jenkins Pipeline
       ↓
Build
       ↓
Test
       ↓
Deploy
       ↓
Run Application
       ↓
Test Application
       ↓
Pipeline Success
5. Expected Result

A successful pipeline should execute all stages and display:

Hello, Jenkins Multi-Stage Pipeline!

The pipeline should finish with:

Pipeline completed successfully!
Finished: SUCCESS
