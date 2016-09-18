import json
import os
import requests

from flask import Flask, request, jsonify

app = Flask(__name__)

VALID_USERS = map(str.strip, filter(
    None, os.environ['VALID_USERS'].split(',')))

HABITICA_API_USER = os.environ['HABITICA_API_USER']
HABITICA_API_KEY = os.environ['HABITICA_API_KEY']


@app.route('/tasks/<task_id>/score/<direction>', methods=['POST'])
def score_task_event(task_id, direction):
    responses = []

    data = request.json
    for commit in data.get('commits', []):
        if commit['author'].get('email') in VALID_USERS or not VALID_USERS:
            responses.append(score_task(task_id, direction))

    return jsonify(responses)


def score_task(task_id, direction):
    habitica_url = 'https://habitica.com/api/v3/tasks/%s/score/%s' % (task_id, direction)

    headers = {
        'x-api-user': HABITICA_API_USER,
        'x-api-key': HABITICA_API_KEY
    }

    return json.loads(requests.post(habitica_url, headers=headers).content)


if __name__ == '__main__':
    app.run()
