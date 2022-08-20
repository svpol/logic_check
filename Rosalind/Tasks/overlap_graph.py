from Rosalind.file_parsers import parse_to_idsec_list
from Rosalind.file_writers import write_list_of_lists


# https://rosalind.info/problems/grph/
# A graph whose nodes have all been labeled can be represented by an adjacency list,
# in which each row of the list contains the two node labels corresponding to a unique edge.
# A directed graph (or digraph) is a graph containing directed edges, each of which has
# an orientation. That is, a directed edge is represented by an arrow instead of a line segment;
# the starting and ending nodes of an edge form its tail and head, respectively. The directed edge
# with tail v and head w is represented by (v,w) (but not by (w,v)). A directed loop is a directed
# edge of the form (v,v).
#
# For a collection of strings and a positive integer k, the overlap graph for the strings is
# a directed graph Ok in which each string is represented by a node, and string s is connected
# to string t with a directed edge when there is a length k suffix of s that matches a length k
# prefix of t, as long as s≠t; we demand s≠t to prevent directed loops in the overlap graph
# (although directed cycles may be present).
#
# Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
# Return: The adjacency list corresponding to O3. You may return edges in any order.
def overlap_graph(sequences: list, k: int = 3) -> list:
    overlap_list = []
    for i in range(len(sequences)):
        j = 0
        while j < len(sequences):
            if j != i:
                if sequences[i][1][-k:] == sequences[j][1][:k]:
                    overlap_list.append([sequences[i][0], sequences[j][0]])
            j += 1
    return overlap_list


if __name__ == "__main__":

    id_seq_list = parse_to_idsec_list('test_data/overlap_graph_test.txt')
    over_graph = overlap_graph(id_seq_list)
    write_list_of_lists(over_graph, 'overlap_graph.txt')
    