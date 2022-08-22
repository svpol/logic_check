from Rosalind.file_parsers import parse_to_intlist


# https://rosalind.info/problems/iev/
# Given: Six nonnegative integers, each of which does not exceed 20,000.
# The integers correspond to the number of couples in a population possessing
# each genotype pairing for a given factor. In order, the six given integers
# represent the number of couples having the following genotypes:
#
# AA-AA
# AA-Aa
# AA-aa
# Aa-Aa
# Aa-aa
# aa-aa
# Return: The expected number of offspring displaying the dominant phenotype
# in the next generation, under the assumption that every couple has exactly two offspring.
def expected_dominant_offspring(integers: list, k: int = 2) -> float:
    dom_offsp = (integers[0] + integers[1] + integers[2] + \
                0.75 * integers[3] + 0.5 * integers[4]) * k
    return dom_offsp


if __name__ == "__main__":

    couple_numbers = parse_to_intlist('test_data/expected_offspring_test.txt')
    print(expected_dominant_offspring(couple_numbers))
