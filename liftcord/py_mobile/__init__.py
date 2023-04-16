from .identify import identify
from discord.gateway import DiscordWebSocket
import logging
from datetime import datetime

class ByteLogger:
    def print(self, text):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logging.info(f"{current_time} INFO {text}")

blog = ByteLogger()
DiscordWebSocket.identify = identify
blog.print("Started liftcord.py-mobile")