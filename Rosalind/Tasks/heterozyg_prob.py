from Rosalind.file_parsers import parse_to_str


# https://rosalind.info/problems/iprb/
# Three positive integers k, m, and n, representing a population containing k+m+n organisms:
# k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
# Count the probability that two randomly selected mating organisms will produce an individual possessing
# a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.
def dominant_allele_prob(k, m, n):
    total = k + m + n
    n_n = (n/total)*((n - 1)/(total - 1))
    m_m = (m/total)*((m - 1)/(total - 1))
    n_m = (n/total)*(m/(total - 1)) + (m/total)*(n/(total - 1))
    dom_prob = 1 - n_n - m_m*0.25 - n_m*0.5
    return dom_prob


if __name__ == "__main__":

    k, m, n = parse_to_str('test_data/heterozyg_prob_test.txt').split()
    print(dominant_allele_prob(int(k), int(m), int(n)))
