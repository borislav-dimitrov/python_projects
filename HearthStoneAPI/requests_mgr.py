import requests
import json
from token_mgr import TOKEN
from cards import CARDS

ACCESS_TOKEN = TOKEN.access_token['access_token']
MAX_RETRY = 3
RETRY_CT = 0

class Requests:
    def request_leaderboards() -> None:
        global RETRY_CT, MAX_RETRY
        url = 'https://us.api.blizzard.com/hearthstone/leaderboard/battlegrounds?region=us&locale=en_US'
        headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
        response = requests.get(url, headers=headers)

        if str(response) == '<Response [200]>':
            pass
        else:
            if RETRY_CT < MAX_RETRY:
                RETRY_CT += 1
                TOKEN.update_access_token()
                Requests.request_leaderboards()
            else:
                RETRY_CT = 0
                print(response)


    def request_cards() -> None:
        global RETRY_CT, MAX_RETRY
        url = 'https://us.api.blizzard.com/hearthstone/cards?locale=en_US&gameMode=battlegrounds'
        headers = {'Authorization': f'Bearer {ACCESS_TOKEN}'}
        response = requests.get(url, headers=headers)

        if str(response) == '<Response [200]>':
            response = response.json()
            pages = response['pageCount']
            page = 1
            while page < pages:
                if not isinstance(response, dict):
                    response = response.json()

                CARDS.collect_cards(response)
                page += 1
                response = requests.get(f'{url}&page={page}', headers=headers)

            if not isinstance(response, dict):
                    response = response.json()

            CARDS.collect_cards(response)

        else:
            if RETRY_CT < MAX_RETRY:
                RETRY_CT += 1
                TOKEN.update_access_token()
                Requests.request_cards()
            else:
                RETRY_CT = 0
                print(response)

        # if CARDS.all:
            # CARDS.process_cards()
