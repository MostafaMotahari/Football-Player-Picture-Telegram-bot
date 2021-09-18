import random
import time

from pyrogram import Client, filters

from base.settings import (
    OWNER, OWNERS,
    ALL_PLAYERS_NAME, USED_PLAYER_NAMES,
    ALL_SEARCH_PLAYER_NAME, USED_SEARCH_PLAYER_NAMES
)
from base.plugins.custom_filters import power_filter


# Send picture
@Client.on_message(filters.user(OWNERS) & power_filter & (filters.regex("/speed$") | filters.regex("/search$")))
def next_picture(cli: Client, msg):
    player_name = ""

    if msg.text == "/speed":
        global ALL_PLAYERS_NAME
        global USED_PLAYER_NAMES
        print(ALL_PLAYERS_NAME)

        if len(ALL_PLAYERS_NAME) == 0:
            ALL_PLAYERS_NAME = USED_PLAYER_NAMES
            USED_PLAYER_NAMES = []

        else:
            player_name = random.choice(ALL_PLAYERS_NAME)
            ALL_PLAYERS_NAME.remove(player_name)
            USED_PLAYER_NAMES.append(player_name)

    elif msg.text == "/search":
        global ALL_SEARCH_PLAYER_NAME
        global USED_SEARCH_PLAYER_NAMES

        if len(ALL_SEARCH_PLAYER_NAME) == 0:
            ALL_SEARCH_PLAYER_NAME = USED_SEARCH_PLAYER_NAMES
            USED_SEARCH_PLAYER_NAMES = []

        else:
            player_name = random.choice(ALL_SEARCH_PLAYER_NAME)
            ALL_SEARCH_PLAYER_NAME.remove(player_name)
            USED_SEARCH_PLAYER_NAMES.append(player_name)

    search_picture = cli.get_inline_bot_results("bing", player_name, offset="1", latitude=0.00001, longitude=0.0001)

    counter_msg = cli.send_message(msg.chat.id, "1️⃣ 🍆")
    time.sleep(0.8)
    counter_msg.edit_text("2️⃣ 🍑")
    time.sleep(0.8)
    counter_msg.edit_text("3️⃣ 💦")
    time.sleep(0.8)

    cli.send_inline_bot_result(
        msg.chat.id,
        search_picture.query_id,
        search_picture.results[0].id
    )

    time.sleep(10.0)
    cli.send_message(msg.chat.id, "▶️ " + player_name)

