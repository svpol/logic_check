from Rosalind.file_parsers import parse_to_str


# https://rosalind.info/problems/revc/
# Write a reverse complement for DNA.
def reverse_complement(dna_str):
    complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reversed_dna_str = dna_str[::-1]
    reversed_complement = ''
    for letter in reversed_dna_str:
        for k in complements.keys():
            if letter == k:
                reversed_complement += complements[k]
    return reversed_complement


if __name__ == "__main__":

    dna_str = parse_to_str('test_data/reverse_complement_test.txt')
    print(reverse_complement(dna_str))