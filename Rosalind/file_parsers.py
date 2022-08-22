def parse_to_str(filepath: str) -> str:
    with open(filepath) as f:
        file_str = f.read()
    return file_str


def parse_to_intlist(filepath: str) -> list:
    with open(filepath) as f:
        num_list = f.read().split()
        for i in range(len(num_list)):
            num_list[i] = int(num_list[i])
        return num_list


def parse_to_line_list(filepath: str) -> list:
    line_list = []
    with open(filepath) as f:
        for line in f.readlines():
            line_list.append(line.strip())
    return line_list


def parse_to_seq_dict(filepath: str) -> dict:
    seq_dict = {}
    with open(filepath) as f:
        for line in f.readlines():
            line = line.strip()
            if line[0] == ">":
                seq_val = ''
                seq_key = line[1:]
            else:
                seq_val += line
                seq_dict[seq_key] = [seq_val]
    return seq_dict


def parse_to_seq_list(filepath: str) -> list:
    sequences = []
    seq = ''
    with open(filepath) as f:
        for line in f.readlines()[1:]:
            line = line.strip()
            if line[0] != '>':
                seq += line
            else:
                sequences.append(seq)
                seq = ''
        sequences.append(seq)
    return sequences


def parse_tab_to_dict(filepath: str) -> dict:
    file_dict = {}
    with open(filepath) as f:
        for line in f:
            key, value = line.split()
            file_dict[key] = value
    return file_dict


def parse_to_idsec_list(filepath: str) -> list:
    idseq_list = []
    with open(filepath) as f:
        i = -1
        for line in f.readlines():
            line = line.strip()
            if line[0] == '>':
                i += 1
                idseq_list.append([line[1:], ''])
            else:
                idseq_list[i][1] += line
    return idseq_list