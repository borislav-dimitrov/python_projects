import json
from flask import Flask, render_template, request
from requests_mgr import Requests
from cards import CARDS


app = Flask(__name__)
app.template_folder = './static'

# region ROUTES
@app.route('/')
def index():
    return render_template('index.html')
# endregion

def poll_cards():
    try:
        Requests.request_cards()

        if CARDS.all:
            CARDS.add_metadata()
            with open('tmp_out.txt', mode='w') as handle:
                CARDS.dump_all(handle)
    except Exception as ex:
        raise ex


def load_cards_from_file(file: str = 'tmp_out.txt'):
    with open(file, mode='r') as handle:
        cards_raw = json.load(handle)

    if cards_raw:
        CARDS.all = cards_raw
        CARDS.process_cards()

def main_func():
    # poll_cards()
    # load_cards_from_file()
    # app.run(debug=True)
    Requests.request_leaderboards()


if __name__ == '__main__':
    main_func()
