# Containerized Full Stack To-Do Application

## Overview

This project demonstrates a production-style containerized full-stack To-Do application built using Flask, MySQL, Nginx, Docker, GitHub Actions, Prometheus, and Grafana.

The project showcases modern DevOps practices such as containerization, CI/CD automation, Docker Hub integration, monitoring, logging, and deployment.

---

## Technology Stack

* Python Flask
* MySQL
* Nginx
* Docker
* Docker Compose
* GitHub Actions
* Docker Hub
* Prometheus
* Grafana

---

## Architecture

Internet → Nginx → Flask → MySQL

Monitoring:

Prometheus → Grafana

CI/CD:

GitHub Actions → Docker Hub

---

## Features

* Create Tasks
* View Tasks
* Health Check API
* Dockerized Deployment
* Multi-Container Architecture
* CI/CD Automation
* Docker Hub Publishing
* Prometheus Monitoring
* Grafana Dashboards
* Logging
* Security Scanning

---

## Start Application

Build and start containers:

```bash
docker compose up -d --build
```

Verify:

```bash
docker compose ps
```

---

## Application URLs

Application:

http://localhost

Health Check:

http://localhost/health

Prometheus:

http://localhost:9090

Grafana:

http://localhost:3000

---

## CI/CD Pipeline

GitHub Actions automatically:

1. Checks out code
2. Installs dependencies
3. Runs tests
4. Builds Docker image
5. Pushes image to Docker Hub

---

## Docker Hub Repository

subin1987/containerised-todo-app

---

## Monitoring

Prometheus collects metrics from the application.

Grafana visualizes application metrics through dashboards.

---


