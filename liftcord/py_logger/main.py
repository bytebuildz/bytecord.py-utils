import logging
from datetime import datetime

class ByteLogger:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)

    def print(self, text):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f"{current_time} INFO {text}")