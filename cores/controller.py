import requests
import cores
import importlib
import modules
from cores import events


def run(url):
    url = cores.validate_url(url)
    if not url:
        events.error("URL must be foo.bar or http://foo.bar or https://foo.bar")
        raise ValueError("Invalid URL format")
    try:
        response = requests.get(url)
        for key, value in response.headers.items():
            events.header_info(value, key)

        all_modules = cores.load_modules(modules)

        for module in all_modules:
            module = importlib.import_module(module)
            checker = module.Action()
            checker.init_target(url, response.headers)
            checker.analysis()

    except KeyboardInterrupt:
        events.error("Stopped by user", "Interrupted")

    except Exception as error:
        events.error(error)
        raise RuntimeError("Error while running program")