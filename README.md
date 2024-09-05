# 🌐 Proxy and User Agent Randomizer

## 📋 Overview

This project provides a basic foundation for web scraping and automation tasks, focusing on proxy support and user agent randomization. It's a quick and simple implementation designed as a starting point for developers who need to make HTTP requests while maintaining some level of anonymity.

## ✨ Key Components

- 🔒 Basic proxy support
- 🎭 Simple user agent randomization
- 📝 Basic logging setup
- 🛠️ WebRequester class for making requests

## 📁 Project Structure

- `utils/web_requester.py`: Main WebRequester class
- `utils/user_agent_randomizer.py`: Generates random user agents
- `utils/proxy_loader.py`: Loads and parses proxies from a file
- `models/proxy.py`: Proxy model class
- `config/logging_config.py`: Logging configuration
- `tests/`: Unit tests for core components
- `resources/proxies.txt`: List of proxies (not included in the repository)
- `main.py`: Example script demonstrating usage

## 🚀 Quick Start

1. Clone the repository:
   ```
   git clone https://github.com/somanV/proxy-user-agent-randomizer.git
   cd proxy-and-user-agent-randomizer
   ```

2. Install requirements:
   ```
   pip install -r requirements.txt
   ```

3. Add proxies to `resources/proxies.txt`:
   ```
   host:port:username:password
   ```

4. Basic usage:

   ```python
   from utils.web_requester import WebRequester
   from utils.proxy_loader import ProxyLoader
   import random

   proxies = ProxyLoader.load_proxies()
   proxy = random.choice(proxies)
   web_requester = WebRequester(proxy)

   response = web_requester.make_request('https://api.ipify.org?format=json')
   print(f"Your IP: {response.json()['ip']}")
   ```

5. To run the example script:
   ```
   python main.py
   ```

## 🧪 Running Tests

To run the unit tests:
```
python -m unittest discover tests
```

## ⚠️ Disclaimer

This is a basic implementation intended as a starting point. It may require additional error handling, optimization, and features for production use.

## 👨‍💻 Author

- GitHub: [@somanV](https://github.com/somanV)

## 📝 License

This project is [MIT](https://opensource.org/licenses/MIT) licensed.