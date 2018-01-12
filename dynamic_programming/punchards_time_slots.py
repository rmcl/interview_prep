class OptimalPunchcarding(object):
    """Dynamic programming solution to find an optimal set of punchcards to run.

    Original problem from: https://medium.freecodecamp.org/demystifying-dynamic-programming-3efafb8d4296

    Take two lists of length n representing n punchcards cost and value. 

    Call "get_most_value_punchcards" with "max_cost" to get a list of y punchcards
    that have maximum value and do not exceed the max_cost
    """

    def __init__(self, punchcard_start_time, punchcard_end_time, punchcard_values):
        self.indexes = list(range(len(punchcard_start_time)))
        self.start_times = punchcard_start_time
        self.end_times = punchcard_end_time
        self.values = punchcard_values

        # sort the indexes such that they are in the order of start-time ~ O(nlogn)ish
        self.indexes = sorted(
            self.indexes,
            key=lambda idx: self.start_times[idx]
        )

    def get_max_value_punchcards(self):
        return self.recursive_soln(0, 0)

    def recursive_soln(self, cur_idx, next_available_time):
        # base case - we have gone through all punchcards. return zero value
        if cur_idx == len(self.indexes):
            return [], 0

        else:
            # try to include the current punchcard
            cur_start_time = self.start_times[self.indexes[cur_idx]]
            cur_end_time = self.end_times[self.indexes[cur_idx]]
            cur_value = self.values[self.indexes[cur_idx]]

            include_val = float('inf') * -1
            if cur_start_time >= next_available_time:
                # We can include this card because it starts after the last card ends
                include_card_indexes, sub_val = self.recursive_soln(cur_idx + 1, cur_end_time)
                include_val = sub_val + cur_value

            # exclude the current punchcard
            exclude_card_indexes, exclude_val = self.recursive_soln(cur_idx + 1, next_available_time)

            if include_val >= exclude_val:
                include_card_indexes.append(self.indexes[cur_idx])
                soln_indexes = include_card_indexes
                soln_value = include_val
            else:
                soln_indexes = exclude_card_indexes
                soln_value = exclude_val

            return soln_indexes, soln_value

if __name__ == '__main__':
    start_times = [0,1,2,0]
    end_times =   [2,2,5,6]
    values =      [3,1,3,5]

    p = OptimalPunchcarding(start_times, end_times, values)
    print(p.get_max_value_punchcards())
