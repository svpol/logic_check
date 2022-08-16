from Rosalind.file_parsers import parse_to_str


# https://rosalind.info/problems/dna/
# Brief description: a file with a DNA sequence is given.
# Count the number of each letter in this sequence.
def letter_count(dna_str):
    letters = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for letter in dna_str:
        for k in letters.keys():
            if letter == k:
                letters[k] += 1
    return letters.values()


if __name__ == "__main__":

    dna_srt = parse_to_str('test_data/letter_count_test.txt')
    print(*letter_count(dna_srt))
