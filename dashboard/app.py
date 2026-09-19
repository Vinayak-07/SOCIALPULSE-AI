import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import streamlit as st, pandas as pd, plotly.express as px, plotly.graph_objects as go
st.set_page_config(page_title="SocialPulse AI", layout="wide")
st.title("SocialPulse AI — Intelligence Dashboard")
st.caption("DEMO MODE · Analytical Indicators Only · Not Verified Threats")
# Load demo data from DB via simple import
from backend.app.db.database import SessionLocal
from backend.app.db.models import SocialPost
with SessionLocal() as db:
    posts = db.query(SocialPost).limit(200).all()
df = pd.DataFrame([{"platform":p.source,"text":p.text[:60],"sentiment":"neutral","engagement":p.engagement_total} for p in posts])
st.metric("Posts", len(posts))
if not df.empty:
    fig = px.bar(df, x="platform", y="engagement", title="Engagement by Platform (Demo)")
    st.plotly_chart(fig)
st.info("Run /api/v1/demo/seed then refresh to load full pipeline data.")
