import configparser

def get_window_height():
    c = configparser.ConfigParser()
    c.read("config.ini")

    h = c['window_size'].getint('window_height')
    if h < 369:
        return 369
    return h

def get_window_width():
    c = configparser.ConfigParser()
    c.read("config.ini")

    w = c["window_size"].getint("window_width")
    if w < 369:
        return 369
    return w

def get_difficulty():
    c = configparser.ConfigParser()
    c.read("config.ini")

    d = c["difficulty"].getint("difficulty")
    if d > 5 or d < 1:
        return 3
    return d