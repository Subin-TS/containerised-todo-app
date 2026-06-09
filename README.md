# Containerized Full Stack To-Do Application

## Project Overview

This project demonstrates a production-style containerized Full Stack To-Do Application built using Flask, MySQL, Nginx, Docker, GitHub Actions, Docker Hub, Prometheus, and Grafana.

The objective of this project is to learn and implement modern DevOps practices including:

* Containerization using Docker
* Multi-container orchestration using Docker Compose
* CI/CD using GitHub Actions
* Docker Hub image publishing
* Monitoring using Prometheus and Grafana
* Logging and Security Scanning
* Production-style deployment

---

# Project Architecture

```text
                           Internet
                               │
                               ▼
                     ┌────────────────┐
                     │     Nginx      │
                     │ Reverse Proxy  │
                     │    Port 80     │
                     └───────┬────────┘
                             │
                             ▼
                     ┌────────────────┐
                     │   Flask App    │
                     │    Python API  │
                     │   Port 5000    │
                     └───────┬────────┘
                             │
                             ▼
                     ┌────────────────┐
                     │     MySQL      │
                     │    Database    │
                     │   Port 3306    │
                     └────────────────┘


Monitoring Stack
────────────────────────────────────

┌─────────────┐
│ Prometheus  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Grafana   │
└─────────────┘
```

---

# Project Workflow

```text
Developer
    │
    ▼
Git Push
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions CI/CD
    │
    ├── Checkout Code
    ├── Install Dependencies
    ├── Run Tests
    ├── Build Docker Image
    └── Push Docker Image
             │
             ▼
         Docker Hub
             │
             ▼
      Production Server
             │
             ▼
      Docker Compose
             │
             ▼
 Nginx → Flask → MySQL
             │
             ▼
 Prometheus → Grafana
```

---

# Project Folder Structure

```text
containerised-todo-app
│
├── app
│   ├── app.py
│   └── requirements.txt
│
├── mysql-init
│   └── init.sql
│
├── nginx
│   └── default.conf
│
├── tests
│   └── test_app.py
│
├── .github
│   └── workflows
│       └── ci-cd.yml
│
├── prometheus.yml
├── Dockerfile
├── docker-compose.yml
├── .gitignore
├── README.md
└── .env
```

---

# Technology Stack

### Application

* Python Flask
* SQLAlchemy
* MySQL

### Web Layer

* Nginx Reverse Proxy

### Containerization

* Docker
* Docker Compose

### CI/CD

* GitHub Actions
* Docker Hub

### Monitoring

* Prometheus
* Grafana

### Testing

* Pytest

### Security

* Trivy
* Safety

---

# Features

* Create To-Do Tasks
* Retrieve To-Do Tasks
* REST API
* Health Check Endpoint
* Dockerized Deployment
* Multi-Container Architecture
* CI/CD Pipeline
* Docker Hub Integration
* Monitoring Dashboard
* Logging Support
* Security Scanning

---

# API Endpoints

## Home

```http
GET /
```

Response

```json
{
  "message": "Todo App Running"
}
```

---

## Health Check

```http
GET /health
```

Response

```json
{
  "status": "healthy"
}
```

---

## Add Task

```http
POST /todo
```

Request

```json
{
  "task": "Learn Docker"
}
```

Response

```json
{
  "status": "created"
}
```

---

## Get Tasks

```http
GET /todo
```

Response

```json
[
  {
    "id": 1,
    "task": "Learn Docker"
  }
]
```

---

# Running the Application

Build and Start Containers

```bash
docker compose up -d --build
```

Check Containers

```bash
docker compose ps
```

View Logs

```bash
docker logs -f todo-app
```

Stop Containers

```bash
docker compose down
```

---

# Monitoring

## Prometheus

Access:

```text
http://localhost:9090
```

Verify Target:

Status → Targets

---

## Grafana

Access:

```text
http://localhost:3000
```

Default Credentials:

```text
Username: admin
Password: admin
```

Connect Grafana to Prometheus and create dashboards for application monitoring.

---

# CI/CD Pipeline

GitHub Actions automatically performs:

* Checkout Code
* Install Dependencies
* Run Tests
* Build Docker Image
* Push Docker Image to Docker Hub

Workflow File:

```text
.github/workflows/ci-cd.yml
```

---

# Docker Hub Repository

```text
subin1987/containerised-todo-app
```

Example Pull:

```bash
docker pull subin1987/containerised-todo-app:v1.0
```

---

# Security Scanning

## Trivy

```bash
trivy image containerized-todo-stack-app
```

## Safety

```bash
safety scan
```

---

# Production Deployment

Clone Repository

```bash
git clone https://github.com/Subin-TS/containerised-todo-app.git
```

Move into Project

```bash
cd containerised-todo-app
```

Start Application

```bash
docker compose up -d
```

Verify

```bash
docker compose ps
```

Health Check

```bash
curl http://localhost/health
```

--
