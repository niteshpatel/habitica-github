import json
import os
import requests

from flask import Flask, request, jsonify

app = Flask(__name__)

USERNAME_WHITELIST = filter(
    None, os.environ['USERNAME_WHITELIST'].split(','))

HABITICA_API_USER = os.environ['HABITICA_API_USER']
HABITICA_API_KEY = os.environ['HABITICA_API_KEY']


@app.route('/tasks/<task_id>/score/<direction>', methods=['POST'])
def score_task_event(task_id, direction):
    responses = []

    if request.is_json:

        data = request.json
        commits = data.get('commits', [])
        for commit in commits:
            author = commit.get('author')
            if author.get('username') in USERNAME_WHITELIST or not USERNAME_WHITELIST:
                content = score_task(task_id, direction).content
                responses.append(json.loads(content))

    return jsonify(responses)


def score_task(task_id, direction):
    habitica_url = 'https://habitica.com/api/v3/tasks/%s/score/%s' % (task_id, direction)

    headers = {
        'x-api-user': HABITICA_API_USER,
        'x-api-key': HABITICA_API_KEY
    }

    return requests.post(habitica_url, headers=headers)


if __name__ == '__main__':
    app.run()
