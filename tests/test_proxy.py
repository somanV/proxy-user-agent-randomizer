import unittest
from models.proxy import Proxy

class TestProxy(unittest.TestCase):
    def test_proxy_init(self):
        proxy = Proxy("example.com", 8080, "user1", "pass1")
        self.assertEqual(proxy.host, "example.com")
        self.assertEqual(proxy.port, 8080)
        self.assertEqual(proxy.username, "user1")
        self.assertEqual(proxy.password, "pass1")

    def test_proxy_str_with_auth(self):
        proxy = Proxy("example.com", 8080, "user1", "pass1")
        self.assertEqual(str(proxy), "user1:pass1@example.com:8080")

    def test_proxy_str_without_auth(self):
        proxy = Proxy("example.com", 8080)
        self.assertEqual(str(proxy), "example.com:8080")

    def test_proxy_to_dict(self):
        proxy = Proxy("example.com", 8080, "user1", "pass1")
        expected_dict = {
            "host": "example.com",
            "port": 8080,
            "username": "user1",
            "password": "pass1"
        }
        self.assertEqual(proxy.to_dict(), expected_dict)

if __name__ == '__main__':
    unittest.main()