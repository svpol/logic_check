from Rosalind.file_parsers import parse_to_str


# https://rosalind.info/problems/fib/
# We have a Fibonacci sequence of rabbits pairs with F1=F2=1 to initiate the sequence. What means that at first month
# there is 1 pair of rabbits. Each pair of rabbits needs a month to get maturity and then mates giving k pairs of
# new offsprings.
# Thus, any given month will contain the rabbits that were alive the previous month, plus any new offspring.
# Given: Positive integers n≤40 and k≤5, where n is the number of months, k is the number of new offspring pairs
# produced by each mature rabbit pair.
# Task: conut the number of rabbit pairs present after n months.
def fib_rabbits(n, k):
    total = 1
    repr = 1
    for i in range(3, n+1):
        total += repr * k
        children = repr * k
        repr = total - children
    return total


if __name__ == "__main__":

    n, k = parse_to_str('test_data/fibonacci_rabbits_test.txt').split()
    print(fib_rabbits(int(n), int(k)))
