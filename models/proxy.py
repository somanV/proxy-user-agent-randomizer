class Proxy:
    def __init__(self, host: str, port: int, username: str, password: str):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def __str__(self):
        auth = f"{self.username}:{self.password}@" if self.username and self.password else ""
        return f"{auth}{self.host}:{self.port}"

    def to_dict(self):
        return {
            "host": self.host,
            "port": self.port,
            "username": self.username,
            "password": self.password
        }
