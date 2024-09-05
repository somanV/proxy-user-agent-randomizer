import os
from typing import List
import re
import logging
from models.proxy import Proxy 

logger = logging.getLogger(__name__)

class ProxyLoader:
    @staticmethod
    def load_proxies(file_path: str = "resources/proxies.txt") -> List[Proxy]:
        logger.debug(f"Attempting to load proxies from file: {file_path}")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Proxy file not found: {file_path}")

        with open(file_path, "r") as file:
            return ProxyLoader._parse_proxies(file.readlines())

    @staticmethod
    def _parse_proxies(lines: List[str]) -> List[Proxy]:
        logger.debug(f"Parsing {len(lines)} lines from proxy file")
        proxies = []
        for line_number, line in enumerate(lines, 1):
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

        logger.info(f"Successfully loaded {len(proxies)} proxies")
        return proxies

    @staticmethod
    def _parse_proxy_line(line: str) -> Proxy:
        pattern = r'^([^:]+):(\d+):([^:]+):(.+)$'
        match = re.match(pattern, line)
        
        if not match:
            raise ValueError("Invalid proxy format")

        host, port, username, password = match.groups()
        
        try:
            port = int(port)
        except ValueError:
            raise ValueError("Invalid port number")

        return Proxy(host, port, username, password)
