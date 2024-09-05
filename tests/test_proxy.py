import unittest
from models.proxy import Proxy

class TestProxy(unittest.TestCase):
    def setUp(self):
        self.host = "example.com"
        self.port = 8080
        self.username = "user1"
        self.password = "pass1"
        self.proxy_with_auth = Proxy(self.host, self.port, self.username, self.password)
        self.proxy_without_auth = Proxy(self.host, self.port)

    def test_proxy_init(self):
        self.assertEqual(self.proxy_with_auth.host, self.host)
        self.assertEqual(self.proxy_with_auth.port, self.port)
        self.assertEqual(self.proxy_with_auth.username, self.username)
        self.assertEqual(self.proxy_with_auth.password, self.password)

    def test_proxy_str_with_auth(self):
        expected = f"{self.username}:{self.password}@{self.host}:{self.port}"
        self.assertEqual(str(self.proxy_with_auth), expected)

    def test_proxy_str_without_auth(self):
        expected = f"{self.host}:{self.port}"
        self.assertEqual(str(self.proxy_without_auth), expected)

    def test_proxy_to_dict(self):
        expected_dict = {
            "host": self.host,
            "port": self.port,
            "username": self.username,
            "password": self.password
        }
        self.assertEqual(self.proxy_with_auth.to_dict(), expected_dict)

if __name__ == '__main__':
    unittest.main()