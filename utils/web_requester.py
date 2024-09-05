import logging
from typing import Dict, Any

import requests

from utils.user_agent_randomizer import UserAgentRandomizer
from models.proxy import Proxy

logger = logging.getLogger(__name__)

class WebRequester:
    def __init__(self, proxy: Proxy):
        self.proxy = proxy
        self.user_agent = UserAgentRandomizer().generate()
        self._log_initialization()

    def make_request(self, url: str, method: str = 'GET', **kwargs: Any) -> requests.Response:
        logger.debug(f"Making {method} request to {url}")
        
        headers = self._prepare_headers(kwargs.pop('headers', {}))
        proxy_dict = self._prepare_proxy_dict()

        response = self._send_request(url, method, headers, proxy_dict, **kwargs)
        self._handle_response(response)
        
        return response

    def _prepare_headers(self, existing_headers: Dict[str, str]) -> Dict[str, str]:
        return {**existing_headers, 'User-Agent': self.user_agent}

    def _prepare_proxy_dict(self) -> Dict[str, str]:
        auth = self._get_auth_string()
        proxy_url = f"{auth}{self.proxy.host}:{self.proxy.port}"
        return {'http': f'http://{proxy_url}', 'https': f'https://{proxy_url}'}

    def _get_auth_string(self) -> str:
        if self.proxy.username and self.proxy.password:
            return f"{self.proxy.username}:{self.proxy.password}@"
        return ""

    def _send_request(self, url: str, method: str, headers: Dict[str, str], 
                      proxy_dict: Dict[str, str], **kwargs: Any) -> requests.Response:
        logger.debug("Sending request...")
        return requests.request(method=method, url=url, headers=headers, 
                                proxies=proxy_dict, **kwargs)

    def _handle_response(self, response: requests.Response) -> None:
        response.raise_for_status()
        logger.debug(f"Request successful. Status code: {response.status_code}")

    def _log_initialization(self) -> None:
        logger.debug(f"WebRequester initialized with proxy: {self.proxy.host}:{self.proxy.port}")
        logger.debug(f"User-Agent: {self.user_agent}")