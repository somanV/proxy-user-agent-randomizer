import unittest
from utils.user_agent_randomizer import UserAgentRandomizer

class TestUserAgentRandomizer(unittest.TestCase):
    def setUp(self):
        self.randomizer = UserAgentRandomizer()

    def test_generate_format(self):
        user_agent = self.randomizer.generate()
        self.assertRegex(user_agent, r'^Mozilla/5\.0 \(.*\).*')

    def test_generate_platform(self):
        user_agent = self.randomizer.generate()
        platform = None
        for p in self.randomizer.platforms:
            if p in user_agent.lower():
                platform = p
                break
        self.assertIsNotNone(platform)
        self.assertIn(platform, self.randomizer.platforms)

    def test_generate_browser(self):
        user_agent = self.randomizer.generate()
        browser = None
        for b in self.randomizer.browsers:
            if b.capitalize() in user_agent:
                browser = b
                break
        self.assertIsNotNone(browser)
        self.assertIn(browser, self.randomizer.browsers)

    def test_generate_version(self):
        user_agent = self.randomizer.generate()
        version_found = False
        for browser in self.randomizer.browsers:
            versions = getattr(self.randomizer, f"{browser}_versions")
            for version in versions:
                if version in user_agent:
                    version_found = True
                    break
            if version_found:
                break
        self.assertTrue(version_found)

    def test_multiple_generations(self):
        user_agents = set(self.randomizer.generate() for _ in range(100))
        self.assertGreater(len(user_agents), 1)  # Ensure we get different user agents

if __name__ == '__main__':
    unittest.main()