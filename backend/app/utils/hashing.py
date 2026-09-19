import hashlib, os
SALTL = os.getenv("ACTOR_SALT","socialpulse-salt")
def hash_actor(actor_id: str) -> str:
    return hashlib.sha256((actor_id + SALTL).encode()).hexdigest()[:32]
