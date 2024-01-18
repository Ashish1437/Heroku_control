from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from daxxop import daxxop as app
from config import BOT_USERNAME, OWNER_ID 
import config
from pyrogram.types import InputMediaVideo
import random 
from pyrogram.types import Message

#⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
#⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯


start_txt = """**
{}
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
          InlineKeyboardButton("๏ʙᴏᴛ ᴄᴏᴅᴇs๏", callback_data="new_callback_data")
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/726169835ed7cdfd5ccf4.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )



#➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪#➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪

#---------------------------------------------------------------
#------------------------------------------------------------------------------------
@app.on_message(filters.command(["help"]) & filters.group)
async def help_command(client, message):
    start_button_link = f"https://t.me/{BOT_USERNAME}?start=your_start_parameter"
    caption = "๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ᴍʏ ʜᴇʟᴘ ᴍᴇɴᴜ ɪɴ ʏᴏᴜʀ ᴘᴍ "

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton("๏ʜᴇʟᴘ๏", url=start_button_link)],
        ]
    )

    await message.reply_text(caption, reply_markup=keyboard)

#------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------------

@app.on_callback_query(filters.regex("new_callback_data"))
async def new_callback_function(_, callback_query):
    await callback_query.edit_message_media(
        media=InputMediaVideo("https://telegra.ph/file/ea3ed3d67df8dfa4dd73d.mp4", has_spoiler=True),
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="๏ ʙᴀᴄᴋ ๏", callback_data="githelp")]
            ]
        ),
    )





#------------------------------------------------------------------------------------
@app.on_callback_query()
def callback_query_handler(client, query):
    if query.data == 'githelp':
        ghelp_text = (
            "๏ ɢɪᴛʜᴜʙ & ʜᴇʀᴏᴋᴜ ᴄᴏɴᴛʀᴏʟ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs ๏\n"
            "➪/start - sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ \n"
            "➪/help -  Dɪsᴘʟᴀʏ ᴛʜɪs ʜᴇʟᴘ ᴍᴇssᴀɢᴇ\n"
            "➪/allrepo - Lɪsᴛ ʏᴏᴜʀ GɪᴛHᴜʙ ʀᴇᴘᴏsɪᴛᴏʀɪᴇs ᴜsᴇ /allrepo daxxteam\n\n"
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

       
