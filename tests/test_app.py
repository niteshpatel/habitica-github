import json
from unittest import TestCase

import requests_mock
from mock import mock

import app


class AppTestCase(TestCase):
    def setUp(self):
        self.apiUser = 'joe'
        self.apiKey = 'secret'

        app.HABITICA_API_USER = self.apiUser
        app.HABITICA_API_KEY = self.apiKey

        self.app = app.app.test_client()

    @requests_mock.mock()
    def test_score_task_event(self, m):
        # arrange
        data = json.dumps({
            'commits': [
                {
                    'author': {
                        'email': 'nitesh'
                    }
                }
            ]})

        expected_response = {'test': 'value'}
        app.score_task = mock.Mock(return_value=expected_response)

        # act
        rv = self.app.post('/tasks/task1/score/up', data=data, content_type='application/json')

        # assert
        # noinspection PyUnresolvedReferences
        app.score_task.assert_called_once_with('task1', 'up')
        json_data = json.loads(rv.data)
        self.assertEqual(json_data, [expected_response])

        @requests_mock.mock()
        def test_score_task(self, m):
            # arrange
            expected_headers = {
                'x-api-user': self.apiUser,
                'x-api-key': self.apiKey
            }

            expected_url = 'https://habitica.com/api/v3/tasks/task1/score/up'

            m.post(requests_mock.ANY, text="{}")

            # act
            app.score_task('task1', 'up')

            # assert
            history = m.request_history
            self.assertEqual(len(history), 1)

            request = history[0]
            self.assertEqual(request.url, expected_url)
            self.assertEqual(request.method, 'POST')
            self.assertDictContainsSubset(expected_headers, request.headers)
