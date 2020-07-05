'''
Given two numbers 'N' and 'S' , find the largest number that can be formed with 'N' digits and whose sum of digits should be equals to 'S'.
'''


def largest_number(num_dig, sum):
    if num_dig == 1 and sum > 9:
        return None
    if sum > 0:
        digit = min(sum, 9)
        ans_remaining = largest_number(num_dig - 1, sum - digit)
        if ans_remaining is None:
            return None
        return str(digit) + ans_remaining
    return '0' + largest_number(num_dig - 1, 0)
