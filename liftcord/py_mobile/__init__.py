from .identify import identify
from discord.gateway import DiscordWebSocket

DiscordWebSocket.identify = identify
print(f"LIFTCORD.PY-TOOLS | Logged into iOS Mobile Presence")