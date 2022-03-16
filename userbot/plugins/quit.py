"""
.kickme
"""
import time

from telethon.tl.functions.channels import LeaveChannelRequest

from mafiabot.utils import admin_cmd


@borg.on(admin_cmd("kickme", outgoing=True))
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("**𝙸 𝙻𝙴𝙰𝚅𝙴𝙳 𝚃𝙷𝙸𝚂 𝙱𝙾𝚁𝙸𝙽𝙶 𝙶𝚁𝙾𝚄𝙿..🤧**")
        time.sleep(1)
        if "-" in str(e.chat_id):
            await borg(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit("**Iz this even a grp..??**")
