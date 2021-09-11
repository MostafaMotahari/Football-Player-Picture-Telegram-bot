from pyrogram import Client, filters
from pyrogram.types import Message
from base.plugins.send_picture import OWNERS

temp_data = {}
msg_scheme = "{}: {}\n"

# Veridy correct answer
@Client.on_message(filters.user(OWNERS) & filters.regex("^**$"))
def verify_answer(cli: Client, msg: Message):
    if msg.reply_to_message:
        winner_user = msg.reply_to_message.from_user.id
        if temp_data[str(msg.chat.id)][str(winner_user)]:
            temp_data[str(msg.chat.id)][str(winner_user)] += 1

        else:
            temp_data[str(msg.chat.id)][str(winner_user)] = 1

        text = "🔅 Points:\n"

        for winners, points in temp_data[str(msg.chat.id)].keys(), temp_data[str(msg.chat.id)].values():
            user = cli.get_users(int(winners))[0]
            text += msg_scheme.format(
                user.first_name,
                str(points)
            )

        msg.reply_text(text)


# Reset points
@Client.on_message(filters.user(OWNERS) & filters.regex("^/reset$"))
def reset_point(cli: Client, msg: Message):
    if msg.chat.id in temp_data.keys():
        temp_data.pop(str(msg.chat.id)
        msg.reply_text("Yay!")