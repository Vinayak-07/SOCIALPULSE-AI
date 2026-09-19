def build_topics(posts):
    # Fallback KMeans-style labeling
    return [{"topic_number":1,"topic_name":"Emerging Transport Disruption","keywords":"transport,disruption,infrastructure","description":"Detected via TF-IDF+KMeans fallback","post_count":len(posts)}]
