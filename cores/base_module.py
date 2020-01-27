from cores import events


class CoreModule(object):
    def __init__(self):
        """
        :self.name: Name of the header value
        :self.url: URL of target (for programming logic only)
        :self.data: Header response of target (programming logic onlY)
        :self.suggestions: List of values should be used by default
        :self.reference: URL of doc
        :self.alert_missing_protocol: List of protocol (http, https)
            the header should be set
        """
        self.name = "Base Module name"
        self.url = ""
        self.data = ""
        self.suggestions = []
        self.description = ""
        self.reference = ""
        self.alert_missing_protocol = []

    def init_target(self, url, data):
        self.url = url
        self.data = data

    def check_values(self):
        status = False
        for suggest in self.suggestions:
            if suggest == self.data[self.name]:
                status = True
                break
        if status == False:
            pass
            # TODO improve warning, error or warn with this

    def analysis(self):
        if self.alert_missing_protocol:
            if self.url.split("://")[0] in self.alert_missing_protocol:
                events.data_error("{} is missing".format(self.name))
                # No value to check. We don't have to validate values
                return True
        self.check_values()
