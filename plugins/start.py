from pyrogram import Client, filters,StopPropagation
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(filters.command(["start"])& filters.private)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("For Movies", url="https://t.me/INDIAHDM0VIES")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/Anshu888o")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
