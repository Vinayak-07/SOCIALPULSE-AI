from backend.app.connectors.base_connector import ConnectorBase
class MastodonConnector(ConnectorBase):
    name = "mastodon"
    def fetch(self, **kw): return []
    def status(self):
        import os
        return {"name":"mastodon","enabled":os.getenv("MASTODON_ENABLED","false").lower()=="true","status":"NOT_CONFIGURED"}
