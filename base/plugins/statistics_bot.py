from pyrogram import Client, filters

from base.settings import OWNER
from base.plugins.utilities import get_all_names, get_all_search_names

# Get statistics of bot
@Client.on_message(filters.user(OWNER) & filters.regex("^/amar$"))
def get_bot_statistics(cli, msg):
    number_of_speeds_names = len(get_all_names())
    number_of_search_names = len(get_all_search_names())

    text = f"تعداد اسم های سرعتی [ {number_of_speeds_names} ]\nتعداد اسم های سرچی [ {number_of_search_names} ]"
    
    msg.reply(text)