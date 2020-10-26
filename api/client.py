import requests


class RestfulBookerClient:

    _s = requests.sessions()
    host = None

    def __init__(self, host):
        self.host = host

    def login(self, username, password):
        data = {"username": username, "password": password}
        return self._s.post(self.host + "/auth", json=data)

    def authorize(self, username, password):
        res = self.login(username, password)
        if res.status_code != 200:
            raise Exception('Unable to authorize using given credentials')
        session_token = res.json().get("token")
        cookie = requests.cookies.create_cookie("token", session_token)

