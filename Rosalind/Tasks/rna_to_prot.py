from Rosalind.file_parsers import parse_to_str, parse_tab_to_dict


# https://rosalind.info/problems/prot/
# Translate a given RNA sequence to the protein.
def translate_rna(rna: str, codons: dict) -> str:
    protein = ''
    i = 0
    while i in range(len(rna) - 2):
        for k in codons.keys():
            if rna[i:i+3] == k:
                if codons[k] != '*':
                    protein += codons[k]
                i += 3
    return protein


if __name__ == "__main__":

    codon_dict = parse_tab_to_dict('../codons_rna.txt')
    rna_str = parse_to_str('test_data/rna_to_prot_test.txt')
    print(translate_rna(rna_str, codon_dict))
