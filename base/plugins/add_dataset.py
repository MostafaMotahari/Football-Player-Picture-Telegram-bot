from pyrogram import Client, filters

from base.plugins.utilities import (
    add_to_dataset,
    get_all_search_names,
    get_all_names
)
from base.settings import (
    OWNER,
    ALL_SEARCH_PLAYER_NAME, USED_SEARCH_PLAYER_NAMES,
    ALL_PLAYERS_NAME, USED_PLAYER_NAMES
)

# Add to dataset
@Client.on_message(filters.user(OWNER) & filters.regex("^/add_dataset_(.*)$") & filters.reply)
def add_new_dataset(cli, msg):
    new_dataset = msg.reply_to_message.download()

    if msg.text.split("_")[-1] == "start":
        add_to_dataset(new_dataset, starts_with=True)

    elif msg.text.split("_")[-1] == "end":
        add_to_dataset(new_dataset, starts_with=False)

    global ALL_PLAYERS_NAME
    ALL_PLAYERS_NAME = get_all_names()
    
    global USED_PLAYER_NAMES
    USED_PLAYER_NAMES = []

    global ALL_SEARCH_PLAYER_NAME
    ALL_SEARCH_PLAYER_NAME = get_all_search_names()

    global USED_SEARCH_PLAYER_NAMES
    USED_SEARCH_PLAYER_NAMES = []

    msg.reply("اسامی جدید با موفقیت اضافه شد!\nبرای حصول اطمینان امار ربات را چک کنید")
