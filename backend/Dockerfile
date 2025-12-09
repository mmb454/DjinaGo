FROM python:3.11-slim

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY backend/ ./

ENV PYTHONUNBUFFERED=1

CMD ["gunicorn", "project_name.wsgi:application", "--bind", "0.0.0.0:8000"]
