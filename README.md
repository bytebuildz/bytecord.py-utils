<br/>
<div align="center">
  <a href="https://github.com/bytebuildz/discord.py-utils">
    <img src="https://discord.com/assets/9f6f9cd156ce35e2d94c0e62e3eff462.png" alt="Logo" width="120" height="120">
  </a>
  
  <h2 align="center">discord.py-ios</h3>

  <p align="center">
    Best discord.py Tools
    <br />
    <br />
    <a href="https://github.com/bytebuildz/discord.py-utils/issues">Report Bug</a>
    ·
    <a href="https://github.com/bytebuildz/discord.py-utils/issues">Request Feature</a>
  </p>
</div>

---------------------------------------

```
pip install -U git+https://github.com/bytebuildz/bytecord.py-utils
```

```py
import bytecord.py_TOOL

import discord
from discord.ext import commands

bot = commands.Bot(...)
```
- All you need todo is import `bytecord.py_TOOL` before any discord.py related 

------------------------------------------

<h2 align="center">Tools</h2>

- bytecord.py_mobile - **Make your boot look diffrent, by giving it Mobile Status**
```py
import bytecord.py_mobile
```
- bytecord.py_gui - discord.py bot control panel gui **(Not Working)**
```py
import bytecord.py_gui
```
- bytecord.py_logger - discord.py Custom logging system **(In-Dev)**
```py
import bytecord.py_logger
```

---------------------------------------

<h2 align="center">Usage</h2>

- bytecord.py_mobile

```py
import bytecord.py_mobile

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents().all())

@bot.event
async def on_ready():
    print("Bot Logged in")

bot.run("token")
```

- bytecord.py_logger

```py
import bytecord.py_logger

import discord
from discord.ext import commands

logger = bytecord.py_logger.ByteLogger()
bot = commands.Bot(command_prefix="!", intents=discord.Intents().all())

@bot.event
async def on_ready():
    logger.print("log")

bot.run("token")
```

- bytecord.py_gui **Not Working**
