import random
import logging
from typing import Dict, List

logger = logging.getLogger(__name__)

class UserAgentRandomizer:
    def __init__(self):
        logger.debug("Initializing UserAgentRandomizer")
        self._initialize_data()

    def _initialize_data(self):
        self.platforms = ['android', 'windows', 'mac', 'iphone', 'linux']
        self.browsers = ['chrome', 'firefox', 'safari', 'edge']
        
        self.versions: Dict[str, List[str]] = {
            'chrome': ['91.0.4472.124', '92.0.4515.159', '93.0.4577.63', '94.0.4606.81'],
            'firefox': ['57.0', '58.0', '59.0', '60.0'],
            'safari': ['600.9', '536.9', '535.2'],
            'edge': ['15.42310', '18.65789'],
            'android': ['6.0.1', '7.1.1'],
            'ios': ['8_5_4', '8_4_8'],
            'windows': ['10.0', '10.3', '10.4'],
            'mac': ['10_5_8', '10_6_8', '10_7_5']
        }
        
        logger.debug(f"Available platforms: {self.platforms}")
        logger.debug(f"Available browsers: {self.browsers}")

    def generate(self) -> str:
        platform = random.choice(self.platforms)
        browser = random.choice(self.browsers)
        
        generator_method = getattr(self, f"_generate_{platform}_ua")
        return generator_method(browser)

    def _generate_android_ua(self, browser: str) -> str:
        android_version = random.choice(self.versions['android'])
        device = random.choice(['Nexus 7', 'LG-H910'])
        chrome_version = random.choice(self.versions['chrome'])
        webkit_version = self._generate_webkit_version()
        
        return f"Mozilla/5.0 (Android {android_version}; {device}) AppleWebKit/{webkit_version} (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/{webkit_version}"

    def _generate_windows_ua(self, browser: str) -> str:
        windows_version = random.choice(self.versions['windows'])
        if browser == 'edge':
            edge_version = random.choice(self.versions['edge'])
            return f"Mozilla/5.0 (Windows NT {windows_version}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/{edge_version}"
        chrome_version = random.choice(self.versions['chrome'])
        return f"Mozilla/5.0 (Windows NT {windows_version}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36"

    def _generate_mac_ua(self, browser: str) -> str:
        mac_version = random.choice(self.versions['mac'])
        if browser == 'firefox':
            firefox_version = random.choice(self.versions['firefox'])
            return f"Mozilla/5.0 (Macintosh; Intel Mac OS X {mac_version}) Gecko/20100101 Firefox/{firefox_version}"
        chrome_version = random.choice(self.versions['chrome'])
        webkit_version = self._generate_webkit_version()
        return f"Mozilla/5.0 (Macintosh; Intel Mac OS X {mac_version}) AppleWebKit/{webkit_version} (KHTML, like Gecko) Chrome/{chrome_version} Safari/{webkit_version}"

    def _generate_iphone_ua(self, browser: str) -> str:
        ios_version = random.choice(self.versions['ios'])
        safari_version = random.choice(self.versions['safari'])
        return f"Mozilla/5.0 (iPhone; CPU iPhone OS {ios_version} like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{safari_version} Mobile/15E148 Safari/{safari_version}"

    def _generate_linux_ua(self, browser: str) -> str:
        chrome_version = random.choice(self.versions['chrome'])
        webkit_version = self._generate_webkit_version()
        return f"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/{webkit_version} (KHTML, like Gecko) Chrome/{chrome_version} Safari/{webkit_version}"

    @staticmethod
    def _generate_webkit_version() -> str:
        return f"{random.randint(530, 603)}.{random.randint(1, 99)}"

    @staticmethod
    def generate_version() -> str:
        return f"{random.randint(1, 20)}.{random.randint(0, 99)}.{random.randint(0, 999)}"
