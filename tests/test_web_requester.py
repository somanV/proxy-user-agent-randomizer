import unittest
from unittest.mock import patch, MagicMock
import requests
from utils.web_requester import WebRequester
from models.proxy import Proxy

class TestWebRequester(unittest.TestCase):

    @patch('utils.web_requester.UserAgentRandomizer')
    def setUp(self, mock_user_agent_randomizer):
        self.proxy = Proxy('127.0.0.1', 8080, 'user', 'pass')
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        mock_user_agent_randomizer.return_value.generate.return_value = self.user_agent
        self.web_requester = WebRequester(self.proxy)
        self.url = 'https://example.com'

    def get_expected_proxies(self):
        return {
            'http': f'http://{self.proxy.username}:{self.proxy.password}@{self.proxy.host}:{self.proxy.port}',
            'https': f'https://{self.proxy.username}:{self.proxy.password}@{self.proxy.host}:{self.proxy.port}'
        }

    @patch('utils.web_requester.requests.request')
    def test_make_request_success(self, mock_request):
        mock_response = MagicMock(status_code=200)
        mock_request.return_value = mock_response

        response = self.web_requester.make_request(self.url)

        self.assertEqual(response, mock_response)
        mock_request.assert_called_once_with(
            method='GET',
            url=self.url,
            proxies=self.get_expected_proxies(),
            headers={'User-Agent': self.user_agent}
        )

    @patch('utils.web_requester.requests.request')
    def test_make_request_with_custom_method_and_params(self, mock_request):
        mock_response = MagicMock(status_code=200)
        mock_request.return_value = mock_response

        params = {'key': 'value'}
        response = self.web_requester.make_request(self.url, method='POST', params=params)

        self.assertEqual(response, mock_response)
        mock_request.assert_called_once_with(
            method='POST',
            url=self.url,
            proxies=self.get_expected_proxies(),
            headers={'User-Agent': self.user_agent},
            params=params
        )

    @patch('utils.web_requester.requests.request')
    def test_make_request_failure(self, mock_request):
        mock_request.side_effect = requests.exceptions.RequestException("Test error")

        with self.assertRaises(requests.exceptions.RequestException):
            self.web_requester.make_request(self.url)

if __name__ == '__main__':
    unittest.main()