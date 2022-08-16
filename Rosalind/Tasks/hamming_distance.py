from Rosalind.file_parsers import parse_to_line_list


# https://rosalind.info/problems/hamm/
# Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t),
# is the number of corresponding symbols that differ in s and t.
# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
# Return: The Hamming distance dH(s,t).
def hamming_distance(s: str, t: str) -> int:
    hamm_dist = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            hamm_dist += 1
    return hamm_dist


if __name__ == "__main__":

    s_str, t_str = parse_to_line_list('test_data/hamming_distance_test.txt')
    print(hamming_distance(s_str, t_str))