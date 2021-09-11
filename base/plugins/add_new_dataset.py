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

        open('a', 'w').writelines(normal_lines)
        open('a', 'w').writelines(hashtag_lines)
