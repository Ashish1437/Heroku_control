from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from daxxop import daxxop as app
from config import BOT_USERNAME
from config import OWNER_ID
import config
import random 
from pyrogram.types import Message

#⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
#⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯


start_txt = """**
๏🤖 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ɢɪᴛʜᴜʙ & ʜᴇʀᴏᴋᴜ ᴄᴏɴᴛʀᴏʟ ʙᴏᴛ! 🚀

๏ᴛʜɪs ʙᴏᴛ sɪᴍᴘʟɪғɪᴇs ʏᴏᴜʀ   
ᴅᴇᴠᴇʟᴏᴘᴍᴇɴᴛ Jᴏᴜʀɴᴇʏ ʙʏ ɪɴᴛᴇɢʀᴀᴛɪɴɢ ɢɪᴛʜᴜʙ ʀᴇᴄᴇɪᴠᴇ ɪɴsᴛᴀɴᴛ ɢɪᴛʜᴜʙ ᴜᴘᴅᴀᴛᴇs ᴀɴᴅ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ʜᴇʀᴏᴋᴜ


๏ᴅᴇᴘʟᴏʏᴍᴇɴᴛs ᴇғғᴏʀᴛʟᴇssʟʏ
ᴛʏᴘᴇ /help ᴛᴏ ᴇxᴘʟᴏʀᴇ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ sᴜᴘᴇʀᴄʜᴀʀɢᴇ ʏᴏᴜʀ ᴡᴏʀᴋғʟᴏᴡ. ʟᴇᴛ's ᴍᴀᴋᴇ ᴄᴏᴅɪɴɢ ᴀɴᴅ ᴅᴇᴘʟᴏʏᴍᴇɴᴛ ᴀ ʙʀᴇᴇᴢᴇ! 💻🔧 #ɢɪᴛʜᴜʙ #ʜᴇʀᴏᴋᴜ #ᴅᴇᴠᴛᴏᴏʟs"
**"""




@app.on_message(filters.command("start"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("๏ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ๏", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("๏sᴜᴘᴘᴏʀᴛ ᴛᴇᴀᴍ๏", url="https://t.me/HEROKUFREECC"),
          InlineKeyboardButton("๏ᴍʏ ᴅᴇᴠʟᴏᴘᴇʀ๏", user_id=config.OWNER_ID)
        ],
        [
          InlineKeyboardButton("๏ʙᴏᴛ ғᴇᴀᴛᴜʀᴇs๏", callback_data="githelp"),
          InlineKeyboardButton("๏ʙᴏᴛ ᴄᴏᴅᴇs๏", callback_data="repo_callback")
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/ecbeac5889f9542f32469.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )



#➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪#➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪#➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪
@app.on_callback_query(filters.regex(r'^repo_callback'))
def handle_repo_callback(client, callback_query):
    user_id = callback_query.from_user.id
    video_file = "https://graph.org/file/52b2315b843584a3c4532.mp4"

    try:
        client.send_video(
            chat_id=user_id,
            video=video_file,
            reply_to_message_id=callback_query.message.message_id
        )
    except Exception as e:
        print(f"Error sending video: {e}")
#➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪

@app.on_callback_query()
def callback_query_handler(client, query):
    if query.data == 'githelp':
        ghelp_text = (
            "๏ ɢɪᴛʜᴜʙ & ʜᴇʀᴏᴋᴜ ᴄᴏɴᴛʀᴏʟ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs ๏\n"
            "➪/start - sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ \n"
            "➪/help -  Dɪsᴘʟᴀʏ ᴛʜɪs ʜᴇʟᴘ ᴍᴇssᴀɢᴇ\n"
            "➪/allrepo - Lɪsᴛ ʏᴏᴜʀ GɪᴛHᴜʙ ʀᴇᴘᴏsɪᴛᴏʀɪᴇs ᴜsᴇ `/allrepo daxxteam`\n\n"
            "➪/create_repo - Cʀᴇᴀᴛᴇ ᴀ ɴᴇᴡ GɪᴛHᴜʙ ʀᴇᴘᴏsɪᴛᴏʀʏ\n"
            "➪/delrepo - Dᴇʟᴇᴛᴇ ᴀ GɪᴛHᴜʙ ʀᴇᴘᴏsɪᴛᴏʀʏ\n"
            "➪/add_collaborator - Aᴅᴅ ᴀ ᴄᴏʟʟᴀʙᴏʀᴀᴛᴏʀ ᴛᴏ ᴀ GɪᴛHᴜʙ ʀᴇᴘᴏsɪᴛᴏʀʏ\n"
            "➪/remove_collaborator - Rᴇᴍᴏᴠᴇ ᴀ ᴄᴏʟʟᴀʙᴏʀᴀᴛᴏʀ ғʀᴏᴍ ᴀ GɪᴛHᴜʙ ʀᴇᴘᴏsɪᴛᴏʀʏ "
        )

        
        buttons = [
            [
                InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data="close_data")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(buttons)

        
        query.message.edit_text(ghelp_text, reply_markup=reply_markup)

#----------------------------------------------------------------------------------------------
#--------------------------------------------------


# Additional callback for closing the message
@app.on_callback_query(filters.regex("^close_data"))
async def close_callback(_, query):
    chat_id = query.message.chat.id
    await query.message.delete()
# incoming msg

@app.on_message(filters.private & filters.incoming)
async def on_pm_s(client: Client, message: Message):
    if not message.from_user.id ==OWNER_ID:
        fwded_mesg = await message.forward(chat_id=OWNER_ID, disable_notification=True)
        
