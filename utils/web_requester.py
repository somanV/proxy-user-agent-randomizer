import requests
from utils.user_agent_randomizer import UserAgentRandomizer
from models.proxy import Proxy
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class WebRequester:
    def __init__(self, proxy: Proxy):
        self.proxy = proxy
        self.user_agent = UserAgentRandomizer().generate()
        logger.debug(f"WebRequester initialized with proxy: {proxy.host}:{proxy.port}")
        logger.debug(f"User-Agent: {self.user_agent}")

    def make_request(self, url: str, method: str = 'GET', **kwargs: Any) -> requests.Response:
        logger.debug(f"Making {method} request to {url}")

        headers = self._prepare_headers(kwargs.get('headers', {}))
        kwargs['headers'] = headers

        proxy_dict = self._prepare_proxy_dict()

        logger.debug("Sending request...")
        response = requests.request(
            method=method,
            url=url,
            proxies=proxy_dict,
            **kwargs
        )
        response.raise_for_status()
        logger.debug(f"Request successful. Status code: {response.status_code}")
        return response

    def _prepare_headers(self, existing_headers: Dict[str, str]) -> Dict[str, str]:
        headers = existing_headers.copy()
        headers['User-Agent'] = self.user_agent
        return headers

    def _prepare_proxy_dict(self) -> Dict[str, str]:
        return {
            'http': f'http://{self.proxy.username}:{self.proxy.password}@{self.proxy.host}:{self.proxy.port}',
            'https': f'https://{self.proxy.username}:{self.proxy.password}@{self.proxy.host}:{self.proxy.port}'
        }