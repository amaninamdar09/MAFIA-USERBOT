# credits to userge
# ported to PANTHERS BOT by @DANISH_BABA
# will be adding more soon

import asyncio
import os
import urllib

import requests

from userbot.Config import Config
from . import *
from mafiabot.utils import *
from userbot.cmdhelp import CmdHelp

@bot.on(admin_cmd("boobs$"))
@bot.on(sudo_cmd(pattern="boobs$", allow_sudo=True))
async def boobs(event):
    if event.fwd_from:
        return
    if not os.path.isdir(Var.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Var.TEMP_DOWNLOAD_DIRECTORY)
    pic_loc = os.path.join(Var.TEMP_DOWNLOAD_DIRECTORY, "bobs.jpg")
    a = await event.reply("Finding some big boobs for u le tharki..🧐")
    await asyncio.sleep(0.5)
    await a.edit("Sending some big boobs tharki sala..🤪")
    nsfw = requests.get("http://api.oboobs.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve("http://media.oboobs.ru/{}".format(nsfw), pic_loc)
    await event.client.send_file(event.chat_id, pic_loc, force_document=False)
    os.remove(pic_loc)
    await event.delete()
    await a.delete()


@bot.on(admin_cmd("butts$"))
@bot.on(sudo_cmd(pattern="butts$", allow_sudo=True))
async def butts(event):
    if event.fwd_from:
        return
    if not os.path.isdir(Var.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Var.TEMP_DOWNLOAD_DIRECTORY)
    pic_loc = os.path.join(Var.TEMP_DOWNLOAD_DIRECTORY, "butts.jpg")
    a = await event.reply("Finding some beautiful butts for u havas ka poojari..🧐")
    await asyncio.sleep(0.5)
    await a.edit("Sending some beautiful butts dekh le gamd..🤪")
    nsfw = requests.get("http://api.obutts.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve("http://media.obutts.ru/{}".format(nsfw), pic_loc)
    await event.client.send_file(event.chat_id, pic_loc, force_document=False)
    os.remove(pic_loc)
    await event.delete()
    await a.delete()

CmdHelp("adultzone").add_command(
  'boobs', None, 'Sends a random boobs pic'
).add_command(
  'butts', None, 'Sends a random Butt pic'
).add_command(
  "xxshort", None, "For Short Se* Videos (Warning 18+ Only) NSFW"
).add_command(
  "xxlong", None, "For Long Se* Video"
).add_command(
  "xnxx", None, "use and see For 18+ only kids don't use"
).add_command(
  "picx", None, "use and see For 18+ only kids don't use"
).add_command(
  "les", None, "use and see For 18+ only kids don't use"
).add_command(
  "xxshort", None, "For Short Se* Videos (Warning 18+ Only) NSFW"
).add_command(
  "xxlong", None, "For Long Se* Video"
).add_warning(
  "For 18+ only kids don't use"
).add()
