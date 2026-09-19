from backend.app.connectors.base_connector import ConnectorBase
class BlueskyConnector(ConnectorBase):
    name = "bluesky"
    def fetch(self, **kw): return []
    def status(self):
        import os
        return {"name":"bluesky","enabled":os.getenv("BLUESKY_ENABLED","true").lower()=="true","status":"READY"}
