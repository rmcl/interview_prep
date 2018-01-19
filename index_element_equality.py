"""Array Index & Element Equality.

Given a sorted array arr of distinct integers, write a function indexEqualsValueSearch that returns the lowest index i for which arr[i] == i. Return -1 if there is no such index. Analyze the time and space complexities of your solution and explain its correctness.

Examples:

input: arr = [-8,0,2,5]
output: 2 # since arr[2] == 2

input: arr = [-1,0,3,6]
output: -1 # since no index in arr satisfies arr[i] == i.
"""


def index_equals_value_search_linear_scan(arr):
    # basic linear scan algo
    for indx in range(len(arr)):
        if indx == arr[indx]:
            return indx
    return -1


def index_equals_value_search(arr):
    """Solution via binary search."""
    start_pos = 0
    end_pos = len(arr)

    min_match_index = float('inf')

    while end_pos >= start_pos:
        # pick the middle element
        pivot = start_pos + (end_pos - start_pos) // 2
        pivot_val = arr[pivot]

        if pivot <= pivot_val:
            if pivot == pivot_val:
                min_match_index = min(
                    pivot,
                    min_match_index
                )

            end_pos = pivot - 1
        else:
            start_pos = pivot + 1

    if min_match_index == float('inf'):
        return -1
    else:
        return min_match_index

if __name__ == '__main__':
    print(index_equals_value_search([-8, 0, 2, 5]))
    print(index_equals_value_search([-1, 0, 3, 6]))
    print(index_equals_value_search([-8, 1, 2, 5]))
