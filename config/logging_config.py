import logging
import os
from logging.handlers import RotatingFileHandler

def configure_logging():
    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)  # Create the log directory if it doesn't exist

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Set the logger to capture all levels of log messages

    # Configure file handler to write logs to a single file with rotation
    file_handler = RotatingFileHandler(
        filename=os.path.join(log_dir, 'app.log'),
        maxBytes=10 * 1024 * 1024,  # 10 MB
        backupCount=5  # Keep up to 5 backup files
    )
    file_handler.setLevel(logging.DEBUG)  # Set file handler to capture debug and above levels
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)  # Set the format for the file handler

    # Configure console handler to write logs to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # Set console handler to capture info and above levels
    console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)  # Set the format for the console handler

    # Add both handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger