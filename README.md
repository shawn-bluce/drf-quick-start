# Django REST Framework Quick Start

A production-ready Django REST Framework boilerplate for building REST APIs quickly and efficiently.

## Overview

This project provides a comprehensive starting template for Django REST Framework applications with essential features and best practices pre-configured. It includes user management, operation logging, asynchronous task processing, and complete Docker deployment setup.

## Key Features

- **Extended User Management** - Enhanced user profiles with social media integration
- **Operation Logging** - Automatic audit trails for all CRUD operations
- **Account Management** - User registration, password reset, and account lock/unlock
- **JWT Authentication** - Secure token-based authentication
- **Asynchronous Tasks** - Celery integration for background job processing
- **API Documentation** - Auto-generated Swagger UI and Redoc documentation
- **Docker Support** - Complete containerization with MySQL and Redis
- **Comprehensive Logging** - Structured logging with error notifications
- **Health Check** - Built-in endpoint for service monitoring

## Tech Stack

- **Python 3.13**
- **Django 6.0**
- **Django REST Framework**
- **MySQL** - Database
- **Redis** - Caching and message broker
- **Celery** - Asynchronous task queue
- **Docker** - Container deployment

## Development Environment
1. clone the repository: `git clone https://github.com/shawn-bluce/drf-quick-start.git`
2. delete the `.git` folder: `rm -rf .git`
3. modify `drf-quick-start` to  your project name in `settings.py`、`wsgi.py`、`uv.lock`、`pyproject.toml` [Optional]
4. modify `fs_project` to your project name wherever you can find it [Optional]
5. install `uv` if you don't have it: `curl -LsSf https://astral.sh/uv/install.sh | sh`
6. install dependencies: `uv install`
7. create `src/fs_project/local_settings.py` and add your local settings (MySQL connection, Redis connection, etc.), this file will be ignored by git and imported in `settings.py`
8. copy `src/.env.example` to `src/.env` and modify the environment variables as needed
9. run `docker compose pull` to pull the MySQL and Redis images if you need
10. create database in MySQL
11. run `uv run python src/manage.py migrate` to create tables
12. run `uv run python src/manage.py createsuperuser` to create a superuser
13. run `uv run python src/manage.py runserver` to start the development server
14. visit `http://127.0.0.1:8000/admin` to access the admin panel, `http://127.0.0.1:8000/api/schema/swagger-ui/` to access the Swagger UI, `http://127.0.0.1:8000/api/schema/redoc/` to access the Redoc UI