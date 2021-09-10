# Imports
from pyrogram import Client, filters
import random
# import csv
import time

# Variables
api_hash = "8b8e85465f15d1100b1e464e2f894ca6"
api_id = 5133796
player_names = []
# with open("player_idlist.csv", "r") as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for row in csv_reader:
#         player_names.append(row['first_name'] + " " + row['second_name'])

cache_name = ""

with open("speeds_player.txt", "r") as players:
    for player in players.readlines():
        player_names.append(player.strip("\n"))

# Main
app = Client(
    "HadsfutBot",
    api_hash=api_hash,
    api_id=api_id,
    # bot_token=bot_token
)

@app.on_message(filters.user(["TheAlternativeMousiol", "God786Ars", "Sajjadmohseni9"]) & filters.regex("/next$"))
def next_picture(cli, msg):
    player_name = random.choice(player_names)
    search_picture = app.get_inline_bot_results("bing", player_name, offset="1", latitude=0.00001, longitude=0.0001)

    app.send_message(msg.chat.id, "1")
    time.sleep(0.5)
    app.send_message(msg.chat.id, "2")
    time.sleep(0.5)
    app.send_message(msg.chat.id, "3")
    time.sleep(0.5)

    app.send_inline_bot_result(
        msg.chat.id,
        search_picture.query_id,
        search_picture.results[0].id
    )

    time.sleep(10.0)
    app.send_message(msg.chat.id, "کونیا اینم جواب  (ریدید رفت):")
    app.send_message(msg.chat.id, player_name)


app.run()