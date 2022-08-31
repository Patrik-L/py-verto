import requests

class Api(object):
    user_agent: str
    refreshToken: str
    access_token: str
    location: str

    def __init__(self, refresh_token: str, location: str, user_agent = None):
        self.refreshToken = refresh_token
        self.location = location
        self.user_agent = user_agent

    def register(self):
        return "done!"

    def refresh_access_token(self) -> dict:
        endpoint = "https://app.vertolive.fi/mobile/v3/refresh"
        data = self.location
        headers = {
                "Authorization": "Bearer " + self.refreshToken,
                "User-Agent": self.user_agent
            }

        r = requests.post(endpoint, json=data, headers=headers)
        data = r.json()
        self.access_token = data["accessToken"]
        return r.json()

    def get_readings(self) -> dict:
        endpoint = "https://app.vertolive.fi/mobile/v3/apartment"
        headers = {
            "Authorization": "Bearer " + self.access_token,
            "User-Agent": self.user_agent
        }
        r = requests.get(endpoint, headers=headers)
        return r.json()