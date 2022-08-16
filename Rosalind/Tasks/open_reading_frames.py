from Rosalind.file_parsers import parse_to_seq_list, parse_tab_to_dict
from reverse_complement import reverse_complement


# https://rosalind.info/problems/orf/
#Either strand of a DNA double helix can serve as the coding strand for RNA transcription.
# Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA
# can be translated into amino acids: three reading frames result from reading the string itself,
# whereas three more result from reading its reverse complement.
# An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without
# any other stop codons in between. Thus, a candidate protein string is derived by translating an open
# reading frame into amino acids until a stop codon is reached.
#
# Given: A DNA string s of length at most 1 kbp in FASTA format. In FASTA format, the string is
# introduced by a line that begins with '>', followed by some labeling information. Subsequent lines
# contain the string itself; the first line to begin with '>' indicates the label of the next string.
#
# Return: Every distinct candidate protein string that can be translated from ORFs of s.
# Strings can be returned in any order.
def orf_translation(dna: str, codons: dict) -> list:
    proteins = []
    i = 0
    orf = False
    i_orf = 0
    while i < len(dna) - 2:
        if dna[i:i + 3] == 'ATG':
            i_orf = i
            orf = True
            protein = codons['ATG']
            i += 3
            while i < len(dna) - 2:
                if dna[i:i + 3] not in ['TAA', 'TAG', 'TGA']:
                    protein += codons[dna[i:i + 3]]
                    i += 3
                else:
                    proteins.append(protein)
                    break
        if orf:
            i = i_orf + 1
            orf = False
        else:
            i += 1
    return proteins


if __name__ == "__main__":

    codons_dna = parse_tab_to_dict('../codons_dna.txt')
    dna_coding = parse_to_seq_list('test_data/open_reading_frames_test.txt')[0]
    dna_template = reverse_complement(dna_coding)
    proteins_coding = orf_translation(dna_coding, codons_dna)
    proteins_template = orf_translation(dna_template, codons_dna)
    print(*list(set(proteins_coding + proteins_template)), sep='\n')
