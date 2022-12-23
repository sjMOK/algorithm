def is_valid(s):
    bracket_mapping = {')': '(', ']': '[', '}': '{'}
    stack = []

    for c in s:
        if c not in bracket_mapping:
            stack.append(c)
        elif not stack or stack.pop() != bracket_mapping[c]:
            return False

    return not stack
