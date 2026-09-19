FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY backend/ ./backend/
COPY dashboard/ ./dashboard/
COPY .env.example .
ENV APP_ENV=development DATA_MODE=demo
EXPOSE 8000 8501
CMD ["bash","-c","python -c 'from backend.app.db.database import init_db; init_db()' && uvicorn backend.app.main:app --host 0.0.0.0 --port 8000"]
