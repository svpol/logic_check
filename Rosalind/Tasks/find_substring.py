from Rosalind.file_parsers import parse_to_line_list


# https://rosalind.info/problems/subs/
# Given a DNA string s and a smaller or equal DNA string t.
# Return all locations (1-based) of t as a substring of s.
def find_substr(string, substring):
    locations = []
    for i in range(len(string) - len(substring) + 1):
        if string[i:i+len(substring)] == substring:
            locations.append(i+1)
    return locations


if __name__ == "__main__":

    s_str, t_substr = parse_to_line_list('test_data/find_substring_test.txt')
    print(*find_substr(s_str, t_substr))