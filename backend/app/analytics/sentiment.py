def analyze(text):
    # Fallback deterministic
    score = min(1.0, len(text)/500)
    neg = score > 0.5
    return {"sentiment":"negative" if neg else "neutral","sentiment_score":score,"model_name":"fallback-deterministic","fallback_used":True}
