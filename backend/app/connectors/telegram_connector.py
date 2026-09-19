from backend.app.connectors.base_connector import ConnectorBase
class TelegramConnector(ConnectorBase):
    name = "telegram"
    def fetch(self, **kw): return []
    def status(self):
        return {"name":"telegram","enabled":False,"status":"DISABLED_BY_DEFAULT"}
