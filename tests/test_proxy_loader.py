import unittest
from unittest.mock import patch
from utils.proxy_loader import ProxyLoader, Proxy

class TestProxyLoader(unittest.TestCase):
    def test_parse_proxies_valid(self):
        mock_lines = ["example.com:8080:user1:pass1", "proxy.net:3128:user2:pass2"]
        proxies = ProxyLoader._parse_proxies(mock_lines)
        self.assertEqual(len(proxies), 2)
        self.assertEqual(proxies[0].to_dict(), Proxy("example.com", 8080, "user1", "pass1").to_dict())
        self.assertEqual(proxies[1].to_dict(), Proxy("proxy.net", 3128, "user2", "pass2").to_dict())

    def test_parse_proxies_invalid_format(self):
        mock_lines = ["invalid_proxy_format", "example.com:8080:user1:pass1"]
        with self.assertRaises(ValueError) as context:
            ProxyLoader._parse_proxies(mock_lines)
        
        self.assertIn("Error parsing proxy on line 1", str(context.exception))
        self.assertIn("Invalid proxy format", str(context.exception))
        self.assertIn("Line content: invalid_proxy_format", str(context.exception))

    def test_parse_proxies_empty_file(self):
        with self.assertRaises(ValueError):
            ProxyLoader._parse_proxies([])

    @patch('os.path.exists')
    def test_load_proxies_file_not_found(self, mock_exists):
        mock_exists.return_value = False
        with self.assertRaises(FileNotFoundError):
            ProxyLoader.load_proxies("non_existent_file.txt")

    def test_parse_proxy_line_valid(self):
        proxy = ProxyLoader._parse_proxy_line("example.com:8080:user1:pass1")
        self.assertEqual(proxy.to_dict(), Proxy("example.com", 8080, "user1", "pass1").to_dict())

    def test_parse_proxy_line_invalid_format(self):
        with self.assertRaises(ValueError):
            ProxyLoader._parse_proxy_line("invalid:format")

    def test_parse_proxy_line_invalid_port(self):
        with self.assertRaises(ValueError):
            ProxyLoader._parse_proxy_line("example.com:invalid:user1:pass1")


if __name__ == '__main__':
    unittest.main()