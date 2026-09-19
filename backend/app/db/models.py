from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, Text, ForeignKey, JSON, LargeBinary
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.app.db.database import Base

class SocialPost(Base):
    __tablename__ = "social_posts"
    id = Column(Integer, primary_key=True)
    source = Column(String)
    source_post_id = Column(String, unique=True, index=True)
    actor_hash = Column(String, index=True)
    text = Column(Text)
    language = Column(String)
    created_at = Column(DateTime)
    url = Column(String)
    reply_to_id = Column(String)
    engagement_total = Column(Float, default=0)
    likes = Column(Integer, default=0)
    reposts = Column(Integer, default=0)
    replies = Column(Integer, default=0)
    views = Column(Integer, default=0)
    data_mode = Column(String, default="DEMO")
    ingested_at = Column(DateTime, default=datetime.utcnow)

class PostEmotion(Base):
    __tablename__ = "post_emotions"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("social_posts.id"))
    sentiment = Column(String)
    sentiment_score = Column(Float)
    emotion = Column(String)
    emotion_score = Column(Float)
    model_name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class Embedding(Base):
    __tablename__ = "embeddings"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("social_posts.id"))
    embedding = Column(LargeBinary)
    model_name = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class Topic(Base):
    __tablename__ = "topics"
    id = Column(Integer, primary_key=True)
    topic_number = Column(Integer)
    topic_name = Column(String)
    keywords = Column(String)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class PostTopic(Base):
    __tablename__ = "post_topics"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("social_posts.id"))
    topic_id = Column(Integer, ForeignKey("topics.id"))
    probability = Column(Float)

class GraphNode(Base):
    __tablename__ = "graph_nodes"
    node_id = Column(String, primary_key=True)
    actor_hash = Column(String, index=True)
    platform = Column(String)
    degree = Column(Integer)
    betweenness = Column(Float)
    pagerank = Column(Float)
    community_id = Column(Integer)

class GraphEdge(Base):
    __tablename__ = "graph_edges"
    source_node = Column(String, ForeignKey("graph_nodes.node_id"), primary_key=True)
    target_node = Column(String, ForeignKey("graph_nodes.node_id"), primary_key=True)
    edge_type = Column(String)
    weight = Column(Float)

class Forecast(Base):
    __tablename__ = "forecasts"
    id = Column(Integer, primary_key=True)
    topic_id = Column(Integer, ForeignKey("topics.id"))
    forecast_time = Column(DateTime)
    predicted_volume = Column(Float)
    lower_bound = Column(Float)
    upper_bound = Column(Float)
    model_name = Column(String)

class Alert(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True)
    alert_type = Column(String)
    severity = Column(String)
    topic = Column(String)
    description = Column(Text)
    metric_value = Column(Float)
    threshold = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    status = Column(String, default="OPEN")

class IngestionRun(Base):
    __tablename__ = "ingestion_runs"
    id = Column(Integer, primary_key=True)
    source = Column(String)
    started_at = Column(DateTime)
    completed_at = Column(DateTime)
    records_fetched = Column(Integer)
    records_stored = Column(Integer)
    status = Column(String)
    error_message = Column(String)

class SystemMetric(Base):
    __tablename__ = "system_metrics"
    id = Column(Integer, primary_key=True)
    metric_name = Column(String)
    metric_value = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
