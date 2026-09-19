def generate_alerts(topics, data):
    alerts = []
    for t in topics:
        if t.get("post_count",0) > 100:
            alerts.append({"id":"A1","alert_type":"Topic Acceleration","severity":"HIGH","topic":t.get("topic_name"),"reason":"Volume increased rapidly vs rolling window","metric_value":t.get("post_count"),"threshold":50,"status":"OPEN"})
    return alerts
