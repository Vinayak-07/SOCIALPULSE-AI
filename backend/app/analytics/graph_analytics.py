import networkx as nx
from backend.app.db.models import GraphNode, GraphEdge

def compute(G):
    degrees = dict(G.degree())
    return {"nodes":len(G.nodes()),"edges":len(G.edges()),"degree":degrees,"message":"Communities are mathematical graph clusters derived from observed public interactions and do not represent verified real-world organizational identities."}
