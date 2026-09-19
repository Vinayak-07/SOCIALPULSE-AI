# SocialPulse AI
AI-driven multi-platform social intelligence. DEMO mode works with zero credentials.

## Env (from .env.example)
DATABASE_URL, YOUTUBE_API_KEY, BLUESKY_ENABLED, MASTODON_ENABLED, TELEGRAM_ENABLED, X_ENABLED, EMBEDDING_MODEL, DATA_MODE

## Run
```
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -c "from backend.app.db.database import init_db; init_db()"
python -c "from backend.app.demo.demo_data_generator import generate; generate()"
uvicorn backend.app.main:app --reload
streamlit run dashboard/app.py
```

## Accept
- DB starts; demo seeds; analytics run; stderr clean; 20+ tests; push to github.com/Vinayak-07/SOCIALPULSE-AI
