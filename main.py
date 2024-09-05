from utils.web_requester import WebRequester
from config.logging_config import configure_logging
from utils.proxy_loader import ProxyLoader
import random

def main():
    logger = configure_logging()

    logger.info("Starting the application")

    try:
        proxies = ProxyLoader.load_proxies()
        logger.info(f"Loaded {len(proxies)} proxies")

        proxy = random.choice(proxies)
        logger.info(f"Selected proxy: {proxy}")
        
        web_requester = WebRequester(proxy)
        
        # Example usage of WebRequester
        response = web_requester.make_request('https://api.ipify.org?format=json')
        logger.info(f"Your IP: {response.json()['ip']}")

    except Exception as e:
        logger.exception(f"An error occurred: {e}")

    logger.info("Application finished")

if __name__ == "__main__":
    main()
