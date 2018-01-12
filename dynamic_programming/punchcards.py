class OptimalPunchcarding(object):
    """Dynamic programming solution to finding an optimal set of punchcards to run
    
    Take two lists of length n representing n punchcards cost and value. 
    
    Call "get_most_value_punchcards" with "max_cost" to get a list of y punchcards
    that have maximum value and do not exceed the max_cost
    
    """
    def __init__(self, punchcard_costs, punchcard_values):
        self.indexes = list(range(len(punchcard_costs)))
        self.costs = punchcard_costs
        self.values = punchcard_values
    
    def get_max_value_punchcards(self, max_cost):
        return self.recursive_soln(0, max_cost)
        
    def recursive_soln(self, cur_idx, max_cost):
        # base case - we have gone through all punchcards. return zero
        if cur_idx == len(self.indexes):
            return [], 0
        
        else:
            
            # we want to try 1) including and 2) excluding the current punchcard.
            cur_cost = self.costs[cur_idx]
            cur_value = self.values[cur_idx]
            
            include_val = float('inf') * -1
            if cur_cost <= max_cost:
                # we can still include this and not exceed the max cost
                include_soln, include_val = self.recursive_soln(cur_idx + 1, max_cost - cur_cost)
            
            # try 2. excluding
            exclude_soln, exclude_val = self.recursive_soln(cur_idx + 1, max_cost)

            if include_val >= exclude_val:               
                include_soln.append(cur_idx)
                soln = include_soln
                value = include_val + cur_value
                
            else:
                soln = exclude_soln
                value = exclude_val
                
            return soln, value

if __name__ == '__main__':

    costs = [1,2,3]
    values = [3,1,3]

    p = OptimalPunchcarding(costs,values)
    p.get_max_value_punchcards(4)
