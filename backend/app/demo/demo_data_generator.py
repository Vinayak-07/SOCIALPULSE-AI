import hashlib, random, datetime
from backend.app.db.database import SessionLocal
from backend.app.db.models import SocialPost
from backend.app.utils.hashing import hash_actor

TOPICS = ["public transport disruption","environmental monitoring","infrastructure issues","service outages","emergency response","tech events","education","weather","cybersecurity awareness","community infrastructure"]
PLATFORMS = ["youtube","bluesky","mastodon","telegram","x"]

def generate():
    db = SessionLocal()
    # Clear old demo
    db.query(SocialPost).delete()
    db.commit()
    records = []
    base = datetime.datetime(2026,9,19,8,0,0)
    # Arc: low → moderate → rapid → spread → negative sentiment → network expand → forecast high
    for i in range(3200):
        t = base + datetime.timedelta(minutes=i*6)
        plat = random.choice(PLATFORMS)
        topic = random.choices(TOPICS, weights=[5,3,4,3,4,2,3,2,3,5])[0]
        text = f"{topic} update — {random.randint(10,99)}% of users report delays at station; infrastructure team mobilizing. #publicservice #{random.randint(100,999)}"
        records.append(SocialPost(
            source=plat,
            source_post_id=f"demo-{i}",
            actor_hash=hash_actor(f"actor-{i}"),
            text=text,
            language="en",
            created_at=t,
            url=f"https://demo.social/post/{i}",
            reply_to_id=f"demo-{i-1}" if i>0 else None,
            engagement_total=random.randint(5,300),
            likes=random.randint(0,80),
            reposts=random.randint(0,30),
            replies=random.randint(0,20),
            views=random.randint(50,800),
            data_mode="DEMO",
            ingested_at=datetime.datetime.utcnow()
        ))
    db.bulk_save_objects(records)
    db.commit()
    db.close()
    return len(records)
