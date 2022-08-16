def write_file(data: list, filepath: str):
    with open(filepath, 'w') as f:
        for i in data:
            f.write(str(i))


def write_file_tab(data: list, filepath: str):
    with open(filepath, 'w') as f:
        for i in data:
            f.write(str(i) + '\t')