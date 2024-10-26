from flask import Flask, render_template, request
from utils import Methods, PollPresets
from managers import CHALLENGES_MGR, CHALLENGES_POLL, result_to_json

app = Flask(__name__)
app.template_folder = './static'


@app.route('/')
def index():
    return render_template('index.html')


@app.route(f'/generate_challenges/{PollPresets.EASY}')
def poll_easy():
    return poll(PollPresets.EASY)


@app.route(f'/generate_challenges/{PollPresets.MEDIUM}')
def poll_medium():
    return poll(PollPresets.MEDIUM)


@app.route(f'/generate_challenges/{PollPresets.HARD}')
def poll_hard():
    return poll(PollPresets.HARD)


@app.route(f'/generate_challenges/{PollPresets.EXTREME}')
def poll_extreme():
    return poll(PollPresets.EXTREME)


@app.route(f'/generate_challenges/{PollPresets.CUSTOM}')
def poll_custom():
    return poll(PollPresets.CUSTOM)


def poll(preset):
    result = CHALLENGES_POLL.poll(preset=preset)

    return {'result': result_to_json(result)}


if __name__ == '__main__':
    CHALLENGES_MGR.load_challenges()
    # ex_poll = CHALLENGES_POLL.poll(preset=PollPresets.EXTREME)
    app.run(debug=True)


# TODO - add shrine restrictions
# TODO - add aura restrictions
# TODO - add merc restrictions
