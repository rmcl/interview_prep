# Add two numbers of potentially great size represented by lists of numbers 0-9
# A = [1, 0, 0]
# B = [1]
# A + B = [1, 0, 1]
# Assume all elements are between 0-9


def add_list_numbers(num1, num2):

    cur_pos = 0
    result = []
    carry = 0
    while len(num1) > cur_pos or len(num2) > cur_pos:

        v1 = 0
        v2 = 0
        if len(num1) > cur_pos:
            v1 = num1[-cur_pos - 1]

        if len(num2) > cur_pos:
            v2 = num2[-cur_pos - 1]

        res = v1 + v2 + carry
        if res > 9:
            carry = 1
            res -= 10
        else:
            carry = 0

        # look that up after
        result.insert(0, res)

        cur_pos += 1

    if carry > 0:
        result.insert(0, carry)

    return result

# Worked example
# A = [(1), 0, 0]
# B = [1]
# cur_pos = 0, carry = 0, result = [1]
# cur_pos = 1, carry = 0, result = [0,1]
# cur_pos = 2, carry = 0, result = [1,0,1]


print(add_list_numbers([1, 0, 0], [1]))
print(add_list_numbers([0, 0, 9], [1]))
print(add_list_numbers([9, 0, 9], [1, 0, 0]))

# Expected output
# [1, 0, 1]
# [0, 1, 0]
# [1, 0, 0, 9]
