from asyncio import sleep

from userbot import *
from mafiabot.utils import admin_cmd


@bot.on(admin_cmd(pattern=r"sdm (\d*) ([\s\S]*)"))
async def selfdestruct(destroy):
    "To self destruct the sent message"
    mafia = ("".join(destroy.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = lion[1]
    ttl = int(lion[0])
    await destroy.delete()
    smsg = await destroy.bot.send_message(destroy.chat_id, message)
    await sleep(ttl)
    await smsg.delete()


@bot.on(admin_cmd(pattern=r"selfdm (\d*) ([\s\S]*)"))
async def selfdestruct(destroy):
    "To self destruct the sent message"
    mafia = ("".join(destroy.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = mafia[1]
    ttl = int(mafia[0])
    text = message + f"\n\n`This message shall be self-destructed in {ttl} seconds`"

    await destroy.delete()
    smsg = await destroy.bot.send_message(destroy.chat_id, text)
    await sleep(ttl)
    await smsg.delete()


@bot.on(admin_cmd(pattern="slfchk$"))
async def oho(event):
    if not event.is_reply:
        return await event.edit("Reply to a self distructing pic !.!.!")
    k = await event.get_reply_message()
    pic = await k.download_media()
    await mafiabot.send_file("me", pic)
    await event.delete()
