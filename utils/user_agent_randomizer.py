import random
import logging

logger = logging.getLogger(__name__)

class UserAgentRandomizer:
    def __init__(self):
        logger.debug("Initializing UserAgentRandomizer")
        self.platforms = ['android', 'windows', 'mac', 'iphone', 'linux']
        self.browsers = ['chrome', 'firefox', 'safari', 'edge']
        
        self.chrome_versions = ['91.0.4472.124', '92.0.4515.159', '93.0.4577.63', '94.0.4606.81']
        self.firefox_versions = ['57.0']
        self.safari_versions = ['600.9', '536.9', '535.2']
        self.edge_versions = ['15.42310', '18.65789']
        
        self.android_versions = ['6.0.1', '7.1.1']
        self.ios_versions = ['8_5_4', '8_4_8']
        self.windows_versions = ['10.0', '10.3', '10.4']
        self.mac_versions = ['10_5_8']
        
        logger.debug(f"Available platforms: {self.platforms}")
        logger.debug(f"Available browsers: {self.browsers}")

    def generate(self):
        platform = random.choice(self.platforms)
        browser = random.choice(self.browsers)
        
        if platform == 'android':
            return self._generate_android_ua(browser)
        elif platform == 'windows':
            return self._generate_windows_ua(browser)
        elif platform == 'mac':
            return self._generate_mac_ua(browser)
        elif platform == 'iphone':
            return self._generate_iphone_ua(browser)
        elif platform == 'linux':
            return self._generate_linux_ua(browser)

    def _generate_android_ua(self, browser):
        android_version = random.choice(self.android_versions)
        device = random.choice(['Nexus 7', 'LG-H910'])
        chrome_version = random.choice(self.chrome_versions)
        webkit_version = f"{random.randint(530, 603)}.{random.randint(1, 99)}"
        
        return f"Mozilla/5.0 (Android; Android {android_version}; {device} Build/MMB29K) AppleWebKit/{webkit_version} (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/{webkit_version}"

    def _generate_windows_ua(self, browser):
        windows_version = random.choice(self.windows_versions)
        if browser == 'edge':
            edge_version = random.choice(self.edge_versions)
            return f"Mozilla/5.0 (Windows; U; Windows NT {windows_version}; Win64; x64) AppleWebKit/600.4 (KHTML, like Gecko) Chrome/52.0.2120.110 Safari/533.6 Edge/{edge_version}"
        else:
            return f"Mozilla/5.0 (Windows; U; Windows NT {windows_version}; WOW64; en-US) AppleWebKit/602.15 (KHTML, like Gecko) Chrome/48.0.3709.173 Safari/603"

    def _generate_mac_ua(self, browser):
        mac_version = random.choice(self.mac_versions)
        if browser == 'firefox':
            firefox_version = random.choice(self.firefox_versions)
            return f"Mozilla/5.0 (Macintosh; U; Intel Mac OS X {mac_version}; en-US) Gecko/20100101 Firefox/{firefox_version}"
        else:
            chrome_version = random.choice(self.chrome_versions)
            webkit_version = f"{random.randint(530, 603)}.{random.randint(1, 99)}"
            return f"Mozilla/5.0 (Macintosh; Intel Mac OS X {mac_version}) AppleWebKit/{webkit_version} (KHTML, like Gecko) Chrome/{chrome_version} Safari/{webkit_version}"

    def _generate_iphone_ua(self, browser):
        ios_version = random.choice(self.ios_versions)
        chrome_version = random.choice(self.chrome_versions)
        webkit_version = f"{random.randint(530, 603)}.{random.randint(1, 99)}"
        
        return f"Mozilla/5.0 (iPhone; CPU iPhone OS {ios_version}; like Mac OS X) AppleWebKit/{webkit_version} (KHTML, like Gecko) Chrome/{chrome_version} Mobile Safari/{webkit_version}"

    def _generate_linux_ua(self, browser):
        chrome_version = random.choice(self.chrome_versions)
        webkit_version = f"{random.randint(530, 603)}.{random.randint(1, 99)}"
        
        return f"Mozilla/5.0 (Linux; U; Linux i546 x86_64) AppleWebKit/{webkit_version} (KHTML, like Gecko) Chrome/{chrome_version} Safari/{webkit_version}"

    def generate_version(self):
        major = random.randint(1, 20)
        minor = random.randint(0, 99)
        patch = random.randint(0, 999)
        return f"{major}.{minor}.{patch}"
