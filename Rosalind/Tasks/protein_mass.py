from Rosalind.file_parsers import parse_to_str, parse_tab_to_dict


# https://rosalind.info/problems/prtm/
# Given: A protein string P of length at most 1000 amino acids
# Return: The total weight of P. Consult the monoisotopic mass table.
def protein_mass(protein: str, amino_acid_mass: dict) -> float:
    prot_mass = 0
    for i in protein:
        for k in amino_acid_mass.keys():
            if i == k:
                prot_mass += float(amino_acid_mass[k])
    return prot_mass


if __name__ == "__main__":

    aa_mass = parse_tab_to_dict('../amino_acid_mass.txt')
    prot = parse_to_str('test_data/protein_mass_test.txt')
    print((protein_mass(prot, aa_mass)))
