# Basic Tech Stack
- Python
- Django
- Django REST framework
- Django filter
- MySQL
- Redis

# Development environment
1. clone the repository: `git clone https://github.com/shawn-bluce/drf-quick-start.git`
2. delete the `.git` folder: `rm -rf .git`
3. modify `drf-quick-start` to  your project name in `settings.py`、`wsgi.py`、`uv.lock`、`pyproject.toml` [Optional]
4. modify `fs_project` to your project name wherever you can find it [Optional]
5. install `uv` if you don't have it: `curl -LsSf https://astral.sh/uv/install.sh | sh`
6. install dependencies: `uv install`
7. create `src/fs_project/local_settings.py` and add your local settings (MySQL connection, Redis connection, etc.), this file will be ignored by git and imported in `settings.py`
8. run `docker compose pull` to pull the MySQL and Redis images if you need
9. create database in MySQL
10. run `uv run python src/manage.py migrate` to create tables
11. run `uv run python src/manage.py createsuperuser` to create a superuser
12. run `uv run python src/manage.py runserver` to start the development server
13. visit `http://127.0.0.1:8000/admin` to access the admin panel, `http://127.0.0.1:8000/api/schema/swagger-ui/` to access the Swagger UI, `http://127.0.0.1:8000/api/schema/redoc/` to access the Redoc UI