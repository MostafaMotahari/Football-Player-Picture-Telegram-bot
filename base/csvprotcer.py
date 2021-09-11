import csv

with open("player_idlist.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    player_names_file = open("player_names.txt", "w")
    player_names = ""
    for row in csv_reader:
        # print(row['first_name'], row['second_name'])
        player_names += row['first_name'] + " " + row['second_name'] + "\n"

    player_names_file.write(player_names)
    player_names_file.close()