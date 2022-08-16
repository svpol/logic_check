from Rosalind.file_parsers import parse_to_seq_list, parse_tab_to_dict
from rna_to_prot import translate_seq


# https://rosalind.info/problems/splc/
# In two words: remove given substrings from a string, then make translation and return the protein.
# In details:
# After identifying the exons and introns of an RNA string, we only need to delete the introns
# and concatenate the exons to form a new string ready for translation.
#
# Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as
# introns. All strings are given in FASTA format. See /test_data/rna_splicing.txt
# Return: A protein string resulting from transcribing and translating the exons of s.
# (Note: Only one solution will exist for the dataset provided.)
def splice_seq(sequences: list) -> str:
    for i in range(1, len(sequences)):
        for j in range(len(sequences[0]) - len(sequences[i]) + 1):
            if sequences[0][j:j+len(sequences[i])] == sequences[i]:
                sequences[0] = sequences[0].replace(sequences[i], '')

    return sequences[0]


if __name__ == "__main__":

    seq_l = parse_to_seq_list('test_data/rna_splicing_test.txt')
    codons_dna = parse_tab_to_dict('../codons_dna.txt')
    spliced_seq = splice_seq(seq_l)
    print(translate_seq(spliced_seq, codons_dna))
