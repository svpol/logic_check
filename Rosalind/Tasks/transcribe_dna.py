from Rosalind.file_parsers import parse_to_str


# https://rosalind.info/problems/rna/
# Brief description: a file with a DNA sequence is given.
# Write a transcribed RNA sequence for it.
def transcribe(dna_str):
    rna_str = ''
    for letter in dna_str:
        if letter == "T":
            rna_str += 'U'
        else:
            rna_str += letter
    return rna_str


if __name__ == "__main__":

    dna_str = parse_to_str('test_data/transcribe_dna_test.txt')
    print(transcribe(dna_str))