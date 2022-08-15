# Find out whether a given integer is present in a given sorted list.
# And, if present, return its index in the sorted list
#
# binary search solution
def binary_search(sorted_list, n):
    for i in range(len(sorted_list)):
        lx = 0
        rx = len(sorted_list) - 1
        while lx <= rx:
            mid = (lx + rx) // 2
            if sorted_list[mid] == n:
                return mid
            elif sorted_list[mid] > n:
                rx = mid - 1
            else:
                lx = mid + 1
    return False


if __name__ == "__main__":

    sorted_l = [-12, -5, -3, 0, 1, 3, 6, 9, 11, 18, 28, 99, 300, 900]
    print(binary_search(sorted_l, 18))
    print(binary_search(sorted_l, -18))
