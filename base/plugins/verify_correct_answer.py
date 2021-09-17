from pyrogram import Client, filters
from pyrogram.types import Message

from base.settings import OWNERS
from base.settings import data as temp_data
from base.plugins.custom_filters import power_filter

# Variables
msg_scheme = "{}: {}\n"

# Veridy correct answer
@Client.on_message(filters.user(OWNERS) & power_filter & filters.regex("^=$") & filters.reply)
def verify_answer(cli: Client, msg: Message):
    global temp_data
    winner_user = msg.reply_to_message.from_user.id
    if str(msg.chat.id) in temp_data.keys():
        if str(winner_user) in temp_data[str(msg.chat.id)].keys():
            temp_data[str(msg.chat.id)][str(winner_user)]\
                ["point"] += 1

        else:
            temp_data[str(msg.chat.id)][str(winner_user)] = {}
            temp_data[str(msg.chat.id)][str(winner_user)]\
                ["point"] = 1

            temp_data[str(msg.chat.id)][str(winner_user)]\
                ["name"] = msg.reply_to_message.from_user.mention

    else:
        temp_data[str(msg.chat.id)] = {}
        temp_data[str(msg.chat.id)][str(winner_user)] = {}
        temp_data[str(msg.chat.id)][str(winner_user)]\
            ["point"] = 1

        temp_data[str(msg.chat.id)][str(winner_user)]\
            ["name"] = msg.reply_to_message.from_user.mention


    text = "🔅 Points:\n"

    for winners in temp_data[str(msg.chat.id)].keys():
        text += msg_scheme.format(
            temp_data[str(msg.chat.id)][str(winners)]["name"],
            temp_data[str(msg.chat.id)][str(winners)]["point"]
        )

    msg.reply_text(text)


# Reset points
@Client.on_message(filters.user(OWNERS) & power_filter & filters.regex("^/reset$"))
def reset_point(cli: Client, msg: Message):
    if str(msg.chat.id) in temp_data.keys():
        temp_data.pop(str(msg.chat.id))
        msg.reply_text("امتیازا ریست شد هعیب.")
