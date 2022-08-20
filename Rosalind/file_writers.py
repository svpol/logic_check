def write_file(data: list, filepath: str):
    with open(filepath, 'w') as f:
        for i in data:
            f.write(str(i))


def write_file_tab(data: list, filepath: str):
    with open(filepath, 'w') as f:
        for i in data:
            f.write(str(i) + '\t')


def write_list_of_lists(some_list: list, filepath: str):
    with open(filepath, 'w') as f:
        for i in some_list:
            for j in i:
                f.write(j + ' ')
            f.write('\n')
