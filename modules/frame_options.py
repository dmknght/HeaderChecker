from cores import base_module


class Action(base_module.CoreModule):
    def __init__(self):
        self.name = "X-Frame-Options"
        self.description = "Avoid Clickjacking attack by ensuring that their content is not embedded into other sites"
        self.suggestions = [
            "X-Frame-Options: deny",  # Block all frame
            "X-Frame-Options: sameorigin",
            # "X-Frame-Options: allow-from uri", # TODO handle uri
        ]
        self.reference = "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options"
        self.alert_missing_protocol = ["http", "https"]
