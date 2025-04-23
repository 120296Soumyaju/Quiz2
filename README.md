# Employee Dashboard API

This Django + DRF application generates, stores, and visualizes synthetic employee data with PostgreSQL.

## 🚀 Features
- Employee + department models
- Attendance and performance records
- REST APIs with filtering and pagination
- Swagger UI for interactive documentation
- PostgreSQL integration

## Tech Stack

- Python 3.13

- Django 3.2+

- Django REST Framework

- PostgreSQL

- drf-yasg

- Faker

- dotenv for config management

## 🛠 Setup Instructions

### 1. Clone Repo & Install Dependencies
```bash
git clone https://github.com/120296Soumyaju/Quiz2.git
cd employee_dashboard
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```
## Quick Start
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py generate_data
python manage.py runserver
```

## API Endpoints

/api/employees/ — CRUD for employees

/api/attendance/ — attendance logs

api/reviews/ - performance reviews

/swagger/ — Swagger UI

/redoc/ — Redoc documentation