import logging
from datetime import datetime

class liftlogger:
    def print(self, text):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f"{current_time} INFO {text}")