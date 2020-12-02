"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No Name set yet. [iqthon.](t.me/iqthon)"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("⌔︙ 🚸 TeleThon For Iraq \n"
                     "⌔︙🔰  Version: 1.0.1\n"
                     # Don't change this else you a TikTok loser, Son of Jinping. Add your own.
                     "⌔︙🔅  Created By: [CH KLANR](https://t.me/RXXRX) || [CH IQ](https://t.me/IQTHON)\n"
                     "⌔︙👾 BOT ORDERS @iraqthonbot\n"
                     "⌔︙ 🗂 The Files : [Here](https://t.me/YZZZY)\n"
                     "⌔︙ Source link ♻️ : [Here](https://heroku.com/deploy?template=https://github.com/klanrali/TeleThon-IRAQ)\n"
                    f"⌔︙👻 My Master : {DEFAULTUSER}\n")
