# CI/CD Final Project

**Project Name:** CI/CD Final Project - Accounts Service  
**Author:** Sanskar Patil  
**Course:** Continuous Integration and Continuous Delivery (CI/CD)  
**Organization:** IBM Developer Skills Network  
**Environment:** Red Hat OpenShift Cluster  

---

## Project Overview
This repository contains the CI/CD pipeline implementation and sample accounts microservice for the final project. It demonstrates end-to-end automation using GitHub Actions for continuous integration, Tekton tasks and pipelines for cloud-native orchestration, and deployment onto an OpenShift cluster.

## Architecture & CI/CD Pipeline
- **Continuous Integration**: Automated GitHub Actions workflow (`.github/workflows/workflow.yml`)
  - Set up job & checkout code
  - Install dependencies
  - Code linting using `flake8`
  - Automated unit testing and code coverage using `nose`
  - Post checkout & complete job
- **Cloud-Native CI/CD**: Tekton & OpenShift Pipelines (`.tekton/tasks.yml`)
  - Workspace cleanup task (`cleanup`)
  - Git clone task (`git-clone`)
  - Linting task (`flake8`)
  - Unit test task (`nose`)
  - Container image build task (`buildah`)
  - Application deployment task (`deploy`)
- **Storage**: PersistentVolumeClaim (`pipelinerun-pvc`) with storage class `skills-network-learner` on OpenShift for workspace persistence across pipeline tasks.

## Project Structure
```text
├── .github/
│   └── workflows/
│       └── workflow.yml
├── .tekton/
│   └── tasks.yml
├── service/
│   ├── __init__.py
│   ├── models.py
│   └── routes.py
├── tests/
│   └── test_routes.py
├── requirements.txt
├── setup.cfg
└── README.md
```

## Running Tests Locally
```bash
nosetests -v --with-spec --spec-color --with-coverage --cover-package=service
```

## Linting
```bash
flake8 service --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 service --count --max-complexity=10 --max-line-length=127 --statistics
```
