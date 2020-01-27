def info(data, info="Info"):
    print("[+] [\033[37m%s\033[00m] %s" % (info, data))


def header_info(data, info="Info"):
    print("[\033[32mHeader\033[00m] [\033[36m%s\033[00m: %s]" % (info, data))


def success(data, info="Done"):
    print("[*] [\033[32m%s\033[00m] [\033[32m%s\033[00m]" % (info, data))


def error(data, info="Error"):
    print("[x] [\033[31m%s\033[00m] %s" % (info, data))


def data_error(data, info="Error"):
    print("[\033[31m%s\033[00m] %s" % (info, data))


def data_warn(name, value, suggestion):
    print("[\033[93m!\033[00m] [\033[32m%s\033: \033[91m%s\033] [Suggest: \033[92m%s\033]" % (name, value, suggestion))
