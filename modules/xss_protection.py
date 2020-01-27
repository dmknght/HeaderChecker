from cores import base_module


class Action(base_module.CoreModule):
    def __init__(self):
        super().__init__()
        self.name = "X-XSS-Protection"
        self.description = "Enable XSS filter in client's browser"
        self.reference = "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection"
        self.alert_missing_protocol = ["http", "https"]
