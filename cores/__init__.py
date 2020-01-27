def validate_url(url):
    """
    Check if URL user gave is an valid Web URL. Return URL with HTTP Protocol if
        URL has no protocol else error
    :param url: string
        Format (http|https)://domain.name:port/foo/bar
    :return: (http|https)://domain.name:port/foo/bar
    """
    if not url:
        return False
    elif url.startswith("http://"):
        return url
    elif url.startswith("https://"):
        return url
    elif "://" in url:
        return False
    else:
        return "http://" + url  # Could be wrong domain name


def load_modules(module_path):
    """
    Load all module in a package dynamically
    :param module_path: string: path to the module to load
    :return: list of module to load by importlib
    """
    import os
    pwd = module_path.__path__[0]

    for root, dirs, files in os.walk(pwd):
        result = filter(lambda x: not x.startswith("__") and x.endswith(".py"), files)

    root = root.split("HeaderChecker/")[1]
    return ["%s.%s" % (root, x.replace(".py", "")) for x in result]
