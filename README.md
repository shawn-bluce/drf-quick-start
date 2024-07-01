# Basic Tech Stack
- Python 3.11
- Django 4.x
- Django REST framework
- Django filter
- MySQL 8.3
- Redis

# Development environment
1. create a virtual environment, for example conda: `conda create -n <your_project_name> python=3.11`
2. activate the virtual environment: `conda activate <your_project_name>`
3. install the required packages: `pip install -r requirements_dev.txt`
4. create local_settings.py to `src/<your_project_name>/local_settings.py`
5. modify the database and other settings in `src/<your_project_name>/local_settings.py`
6. run the database and redis server `docker compose up`
7. migrate the database `python src/manage.py migrate`
8. run the server `python src/manage.py runserver`
