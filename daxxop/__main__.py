import asyncio
import importlib
from pyrogram import idle
from daxxop import daxxop
from daxxop.modules import ALL_MODULES

LOGGER_ID = -1001802990747

loop = asyncio.get_event_loop()

async def daxxpapa_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("daxxop.modules." + all_module)
    print("»»»» ʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ. ✨ 🎉")
    await idle()
    print("»» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")
    await daxxop.send_message(LOGGER_ID, "**ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ !\n Mʏ Dᴇᴠᴇʟᴏᴘᴇʀ  [𝐌𝚁°᭄𝐃𝙰𝚇𝚇 ࿐™ ](https://t.me/iam_daxx)**")

if __name__ == "__main__":
    loop.run_until_complete(daxxpapa_boot())
    
