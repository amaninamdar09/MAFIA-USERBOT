# Credits @buddhhu
#This software is a part of https://github.com/buddhhu/Plus
# Ported to DC by @hellboi_atul

import pygments, os, asyncio
from pygments.lexers import Python3Lexer
from pygments.formatters import ImageFormatter
from userbot.utils import admin_cmd
from userbot import bot as borg
@borg.on(admin_cmd(pattern="ncode ?(.*)"))
async def coder_print(event):
	a = await event.client.download_media(await event.get_reply_message(), Var.TEMP_DOWNLOAD_DIRECTORY)
	s = open(a, 'r')
	c = s.read()
	s.close()
	pygments.highlight(f"{c}", Python3Lexer(), ImageFormatter(font_name="DejaVu Sans Mono", line_numbers=True), "out.png")
	res = await event.client.send_message(event.chat_id, "**𝙿𝚊𝚜𝚝𝚒𝚗𝚐 𝚝𝚑𝚒𝚜 𝚌𝚘𝚍𝚎 𝚊𝚗𝚍 𝚐𝚒𝚟𝚒𝚗𝚐 𝚢𝚘𝚞 𝚘𝚞𝚝𝚙𝚞𝚝 𝚙𝚕𝚣 𝚠𝚊𝚒𝚝 𝚜𝚒𝚛..🤓**", reply_to=event.reply_to_msg_id)
	await event.client.send_file(event.chat_id, "out.png", force_document=True, reply_to=event.reply_to_msg_id, caption="ᴏᴜᴛᴘᴜᴛ ʙʏ [ᴍᴀꜰɪᴀʙᴏᴛ](t.me/MafiaBot_Support)")	
	await res.delete()
	await event.delete()
	os.remove(a)
	os.remove('out.png')
