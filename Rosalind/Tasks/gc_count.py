from Rosalind.file_parsers import parse_to_seq_dict


# https://rosalind.info/problems/gc/
# Given: At most 10 DNA strings in FASTA* format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
# *In FASTA format, the string is introduced by a line that begins with '>', followed by some labeling
# information. Subsequent lines contain the string itself; the first line to begin with '>' indicates
# the label of the next string. See /Rosalind/Tasks/test_data/gc_count_test.txt as an example.
def count_gc(seq_dict: dict) -> list:
    gc_counts = []
    for v in seq_dict.values():
        gc = 0
        for i in v[0]:
            if i == 'C' or i == 'G':
                gc += 1
        gc_count = str(round((gc / len(v[0]) * 100), 6))
        v.append(gc_count)
        gc_counts.append(gc_count)
    max_gc = max(gc_counts)
    for key, value in seq_dict.items():
        if value[1] == max_gc:
            return [key, value[1]]


if __name__ == "__main__":

    seq_d = parse_to_seq_dict('test_data/gc_count_test.txt')
    print(*count_gc(seq_d), sep='\n')
