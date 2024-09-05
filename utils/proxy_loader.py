import os
import re
import logging
from typing import List
from models.proxy import Proxy

logger = logging.getLogger(__name__)

class ProxyLoader:
    @staticmethod
    def load_proxies(file_path: str = "resources/proxies.txt") -> List[Proxy]:
        logger.debug(f"Loading proxies from file: {file_path}")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Proxy file not found: {file_path}")

        with open(file_path, "r") as file:
            return ProxyLoader._parse_proxies(file)

    @staticmethod
    def _parse_proxies(file) -> List[Proxy]:
        proxies = []
        for line_number, line in enumerate(file, 1):
            line = line.strip()
            if not line:
                logger.debug(f"Skipping empty line {line_number}")
                continue

            try:
                proxy = ProxyLoader._parse_proxy_line(line)
                proxies.append(proxy)
                logger.debug(f"Successfully parsed proxy on line {line_number}: {proxy}")
            except ValueError as e:
                raise ValueError(f"Error parsing proxy on line {line_number}: {e}. Line content: {line}")

        if not proxies:
            raise ValueError("No valid proxies found in the file")

        logger.debug(f"Successfully loaded {len(proxies)} proxies")
        return proxies

    @staticmethod
    def _parse_proxy_line(line: str) -> Proxy:
        pattern = r'^([^:]+):(\d+):([^:]+):(.+)$'
        match = re.match(pattern, line)
        
        if not match:
            raise ValueError("Invalid proxy format")

        host, port, username, password = match.groups()
        return Proxy(host, int(port), username, password)
