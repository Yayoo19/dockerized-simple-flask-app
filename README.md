# Docker Flask App Demo

This repository contains a dockerized simple flask app

## Requirements

- Docker

## How to run this repository

- Create image from Dockerfile:

```bash
docker build -t simple-app-image .
```

- Create container using:

```bash
docker run -d -p 5000:5000 --name simple-app-container simple-app-image
```
