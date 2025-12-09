# DjinaGo — Motorcycle Rideshare (MVP)

DjinaGo is a motorcycle rideshare service (MVP) focused on Chad (mobile and driver apps with a Django REST backend and Flutter mobile client).

Key goals (MVP)
- Rider: request a nearby motorcycle, track driver arrival, pay in-app (cash / mobile / card), rate driver.
- Driver: receive nearby requests, accept/decline, navigate to pickup and destination, receive payments.
- Real-time updates for driver location and ride state.

Recommended stack
- Backend: Django + Django REST Framework, Django Channels (WebSocket) for realtime, PostgreSQL, Redis.
- Mobile: Flutter for cross-platform mobile app.
- Payments: Stripe for cards, local mobile money providers (Airtel Money, MoovCash) and cash handling.
- Deployment: Docker, Gunicorn + nginx, managed DB (AWS RDS / Railway / Render).

Quick local dev (backend)
1. cp .env.example .env and fill in SECRET_KEY, DATABASE_URL, REDIS_URL, STRIPE keys.
2. python -m venv .venv && source .venv/bin/activate
3. pip install -r backend/requirements.txt
4. python manage.py migrate
5. python manage.py createsuperuser
6. python manage.py runserver

Next steps after scaffold
- Wire driver verification flows and payment connectors for Chad (Airtel Money / MoovCash)
- Build Flutter screens for rider and driver
- Connect realtime driver location via WebSockets
