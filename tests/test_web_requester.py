import unittest
import requests
from unittest.mock import patch, MagicMock
from utils.web_requester import WebRequester
from models.proxy import Proxy

class TestWebRequester(unittest.TestCase):

    @patch('utils.web_requester.UserAgentRandomizer')
    def setUp(self, mock_user_agent_randomizer):
        self.mock_proxy = Proxy('127.0.0.1', 8080, 'user', 'pass')
        self.mock_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        mock_user_agent_randomizer.return_value.generate.return_value = self.mock_user_agent
        self.web_requester = WebRequester(self.mock_proxy)

    @patch('utils.web_requester.requests.request')
    def test_make_request_success(self, mock_request):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        url = 'https://example.com'
        response = self.web_requester.make_request(url)

        self.assertEqual(response, mock_response)
        mock_request.assert_called_once_with(
            method='GET',
            url=url,
            proxies={
                'http': f'http://user:pass@127.0.0.1:8080',
                'https': f'https://user:pass@127.0.0.1:8080'
            },
            headers={'User-Agent': self.mock_user_agent}
        )

    @patch('utils.web_requester.requests.request')
    def test_make_request_with_custom_method_and_params(self, mock_request):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_request.return_value = mock_response

        url = 'https://example.com'
        params = {'key': 'value'}
        response = self.web_requester.make_request(url, method='POST', params=params)

        self.assertEqual(response, mock_response)
        mock_request.assert_called_once_with(
            method='POST',
            url=url,
            proxies={
                'http': f'http://user:pass@127.0.0.1:8080',
                'https': f'https://user:pass@127.0.0.1:8080'
            },
            headers={'User-Agent': self.mock_user_agent},
            params=params
        )

    @patch('utils.web_requester.requests.request')
    def test_make_request_failure(self, mock_request):
        mock_request.side_effect = requests.exceptions.RequestException("Test error")

        url = 'https://example.com'
        with self.assertRaises(requests.exceptions.RequestException):
            self.web_requester.make_request(url)

if __name__ == '__main__':
    unittest.main()