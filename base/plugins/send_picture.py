from pyrogram import Client, filters
from base.plugins.get_names import get_all_names
import random
import time

# Variables
ALL_NAMES_PLAYER = get_all_names()
print(ALL_NAMES_PLAYER)
OWNERS = [
    "TheAlternativeMousiol",
    "God786Ars",
    "Sajjadmohseni9",
    "spursmylove",
    "Matinieimposter"
]
USED_NAMES = []

# Send picture
@Client.on_message(filters.user(OWNERS) & filters.regex("/next$"))
def next_picture(cli: Client, msg):
    if len(ALL_NAMES_PLAYER) == 0:
        ALL_NAMES_PLAYER = USED_NAMES
        USED_NAMES = []

    else:
        player_name = random.choice(ALL_NAMES_PLAYER)
        ALL_NAMES_PLAYER.remove(player_name)
        USED_NAMES.append(player_name)

    search_picture = cli.get_inline_bot_results("bing", player_name, offset="1", latitude=0.00001, longitude=0.0001)

    counter_msg = cli.send_message(msg.chat.id, "1️⃣ ❗️")
    time.sleep(0.5)
    counter_msg.edit_text("2️⃣ ✅")
    time.sleep(0.5)
    counter_msg.edit_text("3️⃣ 🔥")
    time.sleep(0.5)

    cli.send_inline_bot_result(
        msg.chat.id,
        search_picture.query_id,
        search_picture.results[0].id
    )

    time.sleep(7.5)
    cli.send_message(msg.chat.id, "▶️ " + player_name)

