import requests
import json



class Token:
    def __init__(self) -> None:
        self.client_id = '8c8d829c65544a44bcda150a773dfc75'
        self.secret = 'RPbNLiSf0xRVrzpdhdkk1x8dVIjG40I8'
        self.token_url = 'https://us.battle.net/oauth/token'
        self.data = {'grant_type': 'client_credentials'}
        self.access_token = {
            'access_token': 'USfiNe5rUAYSXEauNPpFNzPRDP6zPsBAxu',
            'token_type': 'bearer',
            'expires_in': 86399,
            'sub': '8c8d829c65544a44bcda150a773dfc75'
        }

    def update_access_token(self):
        response = requests.post(
            self.token_url, data=self.data, auth=(self.client_id, self.secret)
            )
        self.access_token = response.json()

TOKEN = Token()
