from bisect import bisect_left, insort_left


# https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?isFullScreen=true
# The task on how to insert an item to a sorted list without resorting after each insertion.
def activity_notifications(expenditure, d):
    notices = 0
    if len(expenditure) <= d:
        return 0
    exp_sorted = sorted(expenditure[:d])
    for i in range(d, len(expenditure)):
        if d % 2 == 0:
            median_val = (exp_sorted[int(d / 2 - 1)] + exp_sorted[int(d / 2)]) / 2
        else:
            median_val = exp_sorted[d // 2]
        if expenditure[i] >= median_val * 2:
            notices += 1
        del exp_sorted[bisect_left(exp_sorted, expenditure[i - d])]
        insort_left(exp_sorted, expenditure[i])
    return notices


# https://www.hackerrank.com/challenges/mark-and-toys/problem?isFullScreen=true&
# Fast sorting algo is applied here.
def sort_list(some_list):
    if len(some_list) < 2:
        return some_list
    else:
        pivot = some_list[0]
        less = [i for i in some_list[1:] if i <= pivot]
        greater = [i for i in some_list[1:] if i > pivot]
        return sort_list(less) + [pivot] + sort_list(greater)


def maximum_toys(prices, k):
    sorted_prices = sort_list(prices)
    toy_sum = 0
    max_toys = 0
    for i in sorted_prices:
        toy_sum += i
        if toy_sum <= k:
            max_toys += 1
    return max_toys


# https://www.hackerrank.com/challenges/crush/problem?isFullScreen=true
# array manipulation and data storage.
def array_manipulation(n, queries):
    manipulation_list = [0 for m in range(n)]
    for i in queries:
        manipulation_list[i[0] - 1] += i[2]
        if i[1] != len(manipulation_list):
            manipulation_list[i[1]] -= i[2]
    maxval = 0
    cur = 0
    for q in manipulation_list:
        cur += q
        if cur > maxval:
            maxval = cur
    return maxval
