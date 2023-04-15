from .identify import identify
from discord.gateway import DiscordWebSocket
import logging
import datetime

class ByteLogger:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)

    def print(self, text):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f"{current_time} INFO {text}")

blog = ByteLogger()
DiscordWebSocket.identify = identify
blog.print("Enabled bytecord.py_mobile | Mobile Status Started")
