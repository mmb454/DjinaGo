# DjinaGo — Motorcycle Rideshare

DjinaGo is a motorcycle rideshare service focused on Chad (mobile and driver apps with a Django REST backend and Flutter mobile client).

Key goals (MVP)
- Rider: request a nearby motorcycle, track driver arrival, pay in-app (cash / mobile / card), rate driver.
- Driver: receive nearby requests, accept/decline, navigate to pickup and destination, receive payments.
- Real-time updates for driver location and ride state.

stack
- Backend: Django + Django REST Framework, Django Channels (WebSocket) for realtime, PostgreSQL, Redis.
- Mobile: Flutter for cross-platform mobile app.
- Payments: Stripe for cards, local mobile money providers (Airtel Money, MoovCash) and cash handling.
- Deployment: Docker, Gunicorn + nginx, managed DB (AWS RDS / Railway / Render).
