import requests


class RestfulBookerClient:

    _s = requests.sessions()
    host = None

    def __init__(self, host):
        self.host = host

    def login(self, username, password):
        data = {"username": username, "password": password}
        return self._s.post(self.host + "/auth", json=data)