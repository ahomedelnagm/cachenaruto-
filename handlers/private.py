from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAItmWD3OC0m03OLIcpSzfiJMCDxm4xJAAKFAwACH8C5V-U9VextES_XIAQ")
    await message.reply_text(
        f"""**مرحبا 🍭 _ {bn} 🎀
يمكنني تشغيل الموسيقى في الدردشة الصوتية الجماعية الخاصة بك.
أضفني إلى مجموعتك وشغل الموسيقى تم التطوير بواسطة..🙂♥ https://t.me/MusicElkeatib!**

        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔨مطور السورس..🙂♥🔨", url="https://t.me/E_l_k_e_a_t_i_b" )
                  ],[
                    InlineKeyboardButton(
                        "جروب الدعم👿", url="https://t.me/Music54Elkeatib"
                    ),
                    InlineKeyboardButton(
                        "قناة البوت", url="https://t.me/MusicElkeatib"
                    )    
                ],[ 
                    InlineKeyboardButton(
                        "➕اضف البوت اللي مجموعتك..🙂♥➕", url="https://t.me/E_l_k_e_a_t_i_b16bot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Yes iᴍ online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊Uᴩᴅᴀᴛᴇs", url="https://t.me/MusicElkeatib")
                ]
            ]
        )
   )
