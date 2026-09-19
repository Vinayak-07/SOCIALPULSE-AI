class ConnectorBase:
    name = "base"
    def fetch(self, **kw):
        raise NotImplementedError
    def status(self):
        return {"name": self.name, "enabled": False, "status": "DISABLED"}
