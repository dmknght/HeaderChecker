from cores import base_module


class Action(base_module.CoreModule):
    def __init__(self):
        self.name = "X-XSS-Protection"
        self.description = "Enable XSS filter in client's browser"
        self.vulnerability = "Cross-site scripting (XSS)"
        self.vuln_id = "CWE 79"
        self.suggestions = [
            "1",
            "1; mode=block",
            # "X-XSS-Protection: 1; report=<reporting-uri>", # TODO handle report
        ]
        self.reference = "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection"
        self.alert_missing_protocol = ["http", "https"]
