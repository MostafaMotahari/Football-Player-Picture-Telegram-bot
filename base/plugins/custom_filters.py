from pyrogram import filters

from base.settings import data

# Check power of bot filter
power_filter = filters.create(lambda _, __, msg: data["power"] == "on")