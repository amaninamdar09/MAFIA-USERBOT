
# Thanks to @D3_krish
# Porting in MafiaBot by @H1M4N5HU0P

import asyncio
import random
from telethon import events, version
from userbot import mafiaversion
from userbot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.cmdhelp import CmdHelp
from userbot.Config import Config
from . import *
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "𝕄𝔸𝔽𝕀𝔸𝔹𝕆𝕋"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

mafia = bot.uid

MAFIA_IMG = Config.ALIVE_PIC or "https://telegra.ph/file/e97d640332ce5eadb3f89.mp4"
pm_caption = "  __**💥 𝐌𝐀𝐅𝐈𝐀 𝐁𝐎𝐓 𝐈𝐒 𝐀𝐋𝐈𝐕𝐄 💥**__\n\n"

pm_caption += f"**━━━━━━━━━━━━━━━━━━**\n\n"
pm_caption += (
    f"             ⚡ 𝐌𝐀𝐒𝐓𝐄𝐑 ⚡\n       **『[𖤍 𝐃𝐀𝐍𝐈𝐒𝐇 𝐁𝐀𝐁𝐀 𖤍](https://t.me/DANISH_BABA)』**\n\n"
)
pm_caption += f"┏━━━━━━━━━━━━━━━━━━\n"
pm_caption += f"┣•➳➠ `Telethon:` `{version.__version__}` \n"
pm_caption += f"┣•➳➠ `Version:` `{mafiaversion}`\n"
pm_caption += f"┣•➳➠ `Sudo:` `{sudou}`\n"
pm_caption += f"┣•➳➠ `𝐂𝐑𝐄𝐀𝐓𝐄𝐑:`\n [𝐇𝐈𝐌𝐀𝐍𝐒𝐇𝐔 𝐎𝐏](https://t.me/H1M4N5HU0P)\n"
pm_caption += f"┣•➳➠ `𝐎𝐖𝐍𝐄𝐑:`\n [𖤍 𝐃𝐀𝐍𝐈𝐒𝐇 𝐁𝐀𝐁𝐀 𖤍](https://t.me/DANISH_BABA)\n"
pm_caption += f"┗━━━━━━━━━━━━━━━━━━\n"
pm_caption += " [✨𝙼𝚈 𝙶𝚁𝙾𝚄𝙿✨](https://t.me/WEFRIENDSCIRCLE) 🔹 [🔰𝚁𝙴𝙿𝙾🔰](https://github.com/MafiaBotOP/MafiaBot)"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    await alive.delete()
    on = await borg.send_file(alive.chat_id, MAFIA_IMG,caption=pm_caption)

    
CmdHelp("alive").add_command(
  "alive", None, "To check am i alive"
).add()
