import pytest
from backend.app.db.database import init_db, SessionLocal
from backend.app.db.models import SocialPost
from backend.app.demo.demo_data_generator import generate
from backend.app.analytics.text_cleaning import clean
from backend.app.analytics.sentiment import analyze
from backend.app.analytics.topic_modeling import build_topics
from backend.app.analytics.graph_analytics import compute
import networkx as nx

def test_demo_seed_and_clean():
    init_db()
    n = generate()
    assert n >= 3000
    db = SessionLocal()
    assert db.query(SocialPost).count() >= 3000
    db.close()

def test_clean():
    assert "transport" in clean("Transport update #public")

def test_sentiment_fallback():
    res = analyze("bad event")
    assert res["model_name"] == "fallback-deterministic"
    assert res["fallback_used"] is True

def test_topics_fallback():
    t = build_topics([])
    assert t[0]["topic_name"]

def test_graph_metrics():
    G = nx.DiGraph(); G.add_edge("A","B")
    res = compute(G)
    assert res["nodes"] == 2
