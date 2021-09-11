file_names = [
    "speeds_player.txt"
]

def get_all_names():
    all_names = []
    for file_name in file_names:
        with open("base/speed_player_names/" + file_name, "r") as read_file:
            for name in read_file.readlines():
                all_names.append(
                    name.strip("\n")
                )

    return all_names