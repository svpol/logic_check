from Rosalind.file_parsers import parse_to_seq_list


# https://rosalind.info/problems/tran/
# For DNA strings s1 and s2 having the same length, their transition/transversion ratio R(s1,s2)
# is the ratio of the total number of transitions to the total number of transversions, where
# symbol substitutions are inferred from mismatched corresponding symbols.
# For transversion and transition explanation refer to https://rosalind.info/glossary/transitiontransversion-ratio/
# Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).
# Return: The transition/transversion ratio R(s1,s2).
def transition_transversion_ratio(seq_list: list) -> float:
    transition_list = ['AG', 'GA', 'CT', 'TC']
    transitions = 0
    transversions = 0
    mut_str =''
    for i in range(len(seq_list[0])):
        if seq_list[0][i] != seq_list[1][i]:
            mut_str += seq_list[0][i] + seq_list[1][i]
            if mut_str in transition_list:
                transitions += 1
            else:
                transversions += 1
            mut_str = ''
    ratio = transitions / transversions
    return ratio


if __name__ == "__main__":

    sequences = parse_to_seq_list('test_data/trans_ratio_test.txt')
    print(transition_transversion_ratio(sequences))