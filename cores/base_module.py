from cores import events


class CoreModule(object):
    def __init__(self):
        self.name = "Base Module name"
        self.url = ""
        self.data = ""
        self.description = ""
        self.reference = ""
        self.alert_missing_protocol = []

    def init_target(self, url, data):
        self.url = url
        self.data = data

    def analysis(self):
        if self.url.split("://")[0] in self.alert_missing_protocol:
            events.data_error("{} is missing".format(self.name))
            pass # TODO handle alert missing here
        # TODO handle value here