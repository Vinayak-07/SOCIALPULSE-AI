from backend.app.connectors.base_connector import ConnectorBase
class XConnector(ConnectorBase):
    name = "x"
    def fetch(self, **kw): return []
    def status(self):
        import os
        return {"name":"x","enabled":os.getenv("X_ENABLED","false").lower()=="true","status":"OPTIONAL_STUB"}
