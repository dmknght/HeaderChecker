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
                # TODO use regex match instead
                status = True
                break
        if not status:
            # give the last suggestion as best suggestion
            events.data_warn(self.name, self.data[self.name], self.suggestions[-1])
            # TODO improve warning, error for wrong value or warn for unnknow value

    def analysis(self):
        if self.alert_missing_protocol:
            if self.url.split("://")[0] in self.alert_missing_protocol:
                if self.name not in self.data.keys():
                    events.data_error("{} is missing".format(self.name))
                    # No value to check. We don't have to validate values
                    return True
        if self.suggestions:
            self.check_values()
