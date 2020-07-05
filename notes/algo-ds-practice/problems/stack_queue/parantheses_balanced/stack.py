from queue import LifoQueue


def is_opening_paran(char):
    return char in '([{'


def get_opening_paran(closing_paran):
    mapping = {')': '(', '}': '{', ']': '['}
    return mapping[closing_paran]


def is_balanced(line):
    stack = LifoQueue()
    idx = 0
    while idx < len(line):
        char = line[idx]
        if is_opening_paran(char):
            stack.put(char)
        else:
            if stack.qsize() == 0:
                return False
            stack_top = stack.get(False)
            if stack_top != get_opening_paran(char):
                return False
        idx += 1
    return stack.qsize() == 0
