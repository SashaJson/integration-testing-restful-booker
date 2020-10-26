import requests


class RestfulBookerClient:

    _s = requests.sessions()
    host = None

    def __init__(self, host):
        self.host = host