from pyrogram import Client, filters
from base.settings import data, OWNER


# Power on or off the bot
@Client.on_message(filters.user(OWNER) & filters.regex("^/off$"))
def power_off(cli, msg):
    global data
    data["power"] = "off"
    msg.reply("خب دیگه خاموش شدم زجه نزنید بای.")


@Client.on_message(filters.user(OWNER) & filters.regex("/on"))
def power_on(cli, msg):
    global data
    data["power"] = "on"
    msg.reply("خب حاجیا سلاپ من برگشتم باهم دکتر بازی کنیم.")
