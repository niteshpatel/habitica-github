import json
import mock
from unittest import TestCase

import requests_mock

import app


class AppTestCase(TestCase):
    def setUp(self):
        self.api_user = 'joe'
        self.api_key = 'secret'
        self.valid_users = 'nitesh'

        self.os_environ_patcher = mock.patch.dict(
            'os.environ', {
                'VALID_USERS': self.valid_users,
                'HABITICA_API_USER': self.api_user,
                'HABITICA_API_KEY': self.api_key,
            })
        self.os_environ_patcher.start()

        self.app = app.app.test_client()

    def tearDown(self):
        self.os_environ_patcher.stop()

    def test_score_task_event(self):
        # arrange
        data = json.dumps({
            'commits': [
                {
                    'author': {
                        'email': self.valid_users
                    }
                }
            ]})

        expected_response = {'test': 'value'}

        # act
        with mock.patch.object(app, 'score_task', mock.Mock(return_value=expected_response)) as mock_score_task:
            rv = self.app.post('/tasks/task1/score/up', data=data, content_type='application/json')

        # assert
        # noinspection PyUnresolvedReferences
        mock_score_task.assert_called_once_with('task1', 'up')
        json_data = json.loads(rv.data)
        self.assertEqual(json_data, [expected_response])

    @requests_mock.mock()
    def test_score_task(self, m):
        # arrange
        expected_headers = {
            'x-api-user': self.api_user,
            'x-api-key': self.api_key
        }

        expected_url = 'https://habitica.com/api/v3/tasks/task1/score/up'

        m.post(requests_mock.ANY, text='{}')

        # act
        app.score_task('task1', 'up')

        # assert
        history = m.request_history
        self.assertEqual(len(history), 1)

        request = history[0]
        self.assertEqual(request.url, expected_url)
        self.assertEqual(request.method, 'POST')
        self.assertDictContainsSubset(expected_headers, request.headers)
