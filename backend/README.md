Backend quick start (Django + DRF)

1. cp .env.example .env and fill in SECRET_KEY, DATABASE_URL, REDIS_URL, STRIPE keys.
2. python -m venv .venv && source .venv/bin/activate
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py createsuperuser
6. python manage.py runserver
