# Containerized Full Stack To-Do Application

## Overview

This project is a Full Stack To-Do Application built using:

* Python Flask
* MySQL Database
* Docker & Docker Compose
* Nginx Reverse Proxy
* GitHub Actions CI/CD
* Docker Hub

The application allows users to create and view tasks through REST APIs.

---

## Architecture

```text
Internet
   │
   ▼
 Nginx
   │
   ▼
Flask App
   │
   ▼
 MySQL

Docker Compose
├── nginx
├── flask-app
└── mysql

CI/CD
GitHub Actions → Docker Hub
```

---

## Project Structure

```text
containerised-todo-stack
│
├── app
│   ├── app.py
│   └── requirements.txt
│
├── nginx
│   └── default.conf
│
├── mysql-init
│   └── init.sql
│
├── tests
│   └── test_app.py
│
├── Dockerfile
├── docker-compose.yml
├── .env
└── README.md
```

---

## Features

* Create To-Do Tasks
* View To-Do Tasks
* MySQL Database Integration
* Dockerized Application
* Nginx Reverse Proxy
* Docker Compose Deployment
* CI/CD with GitHub Actions
* Docker Hub Integration
* Health Checks
* Logging & Monitoring
* Security Scanning with Trivy

---

## Prerequisites

* Docker
* Docker Compose
* Git
* GitHub Account
* Docker Hub Account

---

## Setup

### Clone Repository

```bash
git clone https://github.com/<Subin-TS>/containerised-todo-app.git
cd containerised-todo-stack
```

### Create Environment File

Create `.env`

```env
DB_HOST=mysql
DB_NAME=todo_db
DB_USER=todo_user
DB_PASSWORD=St***********
MYSQL_ROOT_PASSWORD=Root*********
```

---

## Deploy Application

Start all containers:

```bash
docker compose up -d
```

Check status:

```bash
docker compose ps
```

---

## API Testing

### Home Page

```bash
curl http://localhost
```

Response:

```json
{
  "message":"Todo App Running"
}
```

### Create Task

```bash
curl -X POST \
-H "Content-Type: application/json" \
-d '{"task":"Learn production level deploy"}' \
http://localhost/todo
```

### View Tasks

```bash
curl http://localhost/todo
```

### Health Check

```bash
curl http://localhost/health
```

---

## Docker Commands

Build Image:

```bash
docker build -t todo-app:v1 .
```

Run Container:

```bash
docker run -d -p 5000:5000 --name todo-app todo-app:v1
```

---

## Unit Testing

Run tests:

```bash
pytest
```

---

## CI/CD Pipeline

GitHub Actions performs:

* Code Checkout
* Dependency Installation
* Unit Testing
* Docker Image Build
* Docker Hub Push

Required GitHub Secrets:

```text
DOCKER_USERNAME
DOCKER_PASSWORD
```

---

## Docker Hub

Login:

```bash
docker login
```

Push Image:

```bash
docker push <dockerhub-username>/todo-app:v1.0
```

Pull Image:

```bash
docker pull <dockerhub-username>/todo-app:v1.0
```

---

## Security

Image Scan:

```bash
trivy image todo-app:v1
```

Dependency Scan:

```bash
safety scan
```

Verify Non-Root User:

```bash
docker exec todo-app whoami
```

Expected Output:

```text
appuser
```

---

## Monitoring

Monitoring can be integrated using:

* Prometheus
* Grafana

Grafana URL:

```text
http://server-ip:3000
```

---

