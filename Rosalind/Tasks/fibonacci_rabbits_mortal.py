from Rosalind.file_parsers import parse_to_str


# https://rosalind.info/problems/fibd/
# We have 1 pair of rabbits initially. It is assumed that each pair of rabbits reaches maturity
# in one month and produces a single pair of offspring (one male, one female) each subsequent month.
# All rabbits live for three months (meaning that they reproduce only twice before dying).
# Given: Positive integers n≤100 and m≤20.
# Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits
# live for m months.
def fib_rabbits_mortal(n, m):
    rabbits = [0, 1, 1]
    for i in range(3, n + 1):
        if i <= m:
            total = rabbits[i - 1] + rabbits[i - 2]
        elif i == m + 1:
            total = rabbits[i - 1] + rabbits[i - 2] - 1
        else:
            total = rabbits[i - 1] + rabbits[i - 2] - rabbits[i - m - 1]
        rabbits.append(total)
    return rabbits[n]


if __name__ == "__main__":

    n, m = parse_to_str('test_data/fibonacci_rabbits_mortal_test.txt').split()
    print(fib_rabbits_mortal(int(n), int(m)))