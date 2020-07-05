def is_balanced(my_string):
    '''
    In every iteration, the innermost brackets get eliminated (replaced with empty string).
    If we end up with an empty string, our initial one was balanced; otherwise, not.
    '''
    brackets = ['()', '{}', '[]']
    while any(x in my_string for x in brackets):
        for br in brackets:
            my_string = my_string.replace(br, '')
    return not my_string


string = "{[]{()}}"
print(is_balanced(string))
