from backend.app.connectors.base_connector import ConnectorBase
class YouTubeConnector(ConnectorBase):
    name = "youtube"
    def fetch(self, **kw): return []
    def status(self):
        return {"name":"youtube","enabled":bool(__import__("os").getenv("YOUTUBE_API_KEY")),"status":"CONFIGURED" if __import__("os").getenv("YOUTUBE_API_KEY") else "NOT_CONFIGURED"}
