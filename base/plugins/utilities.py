
from pyrogram import filters
import base.settings as settings

# Get list of admins from admins file
def get_admins_list():
    admins_list = []

    for admin in open('base/data/admins_file.txt', 'r').readlines():
        admins_list.append(
            admin.strip('\n')
        )

    return admins_list

# Get all player names
speed_file_names = []
for file_name in open('base/data/speed_dataset_address.txt', 'r').readlines():
    speed_file_names.append(
        file_name.strip('\n')
    )

search_file_names = []
for file_name in open('base/data/search_dataset_address.txt', 'r').readlines():
    search_file_names.append(
        file_name.strip('\n')
    )

def get_all_names():
    all_names = []
    for file_name in speed_file_names:
        with open(file_name, "r") as read_file:
            for name in read_file.readlines():
                all_names.append(
                    name.strip("\n")
                )

    return all_names

def get_all_search_names():
    all_names = []
    for file_name in search_file_names:
        with open(file_name, "r") as read_file:
            for name in read_file.readlines():
                all_names.append(
                    name.strip("\n")
                )

    return all_names

# Add new dateset
def add_to_dataset(file_path: str):
    with open(file_path, 'r') as read_dataset:
        lines = read_dataset.readlines()
        normal_lines = []
        hashtag_lines = []

        for line in lines:
            if not line.startswith("#"):
                normal_lines.append(
                    line
                )

            else:
                hashtag_lines.append(
                    line[1:]
                )

        open('base/data/speed_player_names/speeds_player.txt', 'a').writelines(normal_lines)
        open('base/data/speed_player_names/search_player.txt.txt', 'a').writelines(hashtag_lines)


# Check power of bot filter
power_filter = filters.create(lambda _, __, msg: settings.data["power"] == "on")
