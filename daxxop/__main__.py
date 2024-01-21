import asyncio
import importlib
from config import LOGGER_ID
from pyrogram import idle
from daxxop import daxxop
from daxxop.modules import ALL_MODULES

 

loop = asyncio.get_event_loop()


async def daxxpapa_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("daxxop.modules." + all_module)
    print("»»»» ʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ. ✨ 🎉")
    await idle()
    print("»» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")
 # --------
await daxxop.send_message(config.LOGGER_ID, "**Bot Started !**")
# -------------
if __name__ == "__main__":
    loop.run_until_complete(daxxpapa_boot())
