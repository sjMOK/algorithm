def remove_duplicate_letters(s):
    stack = []

    for i, char in enumerate(s):
        if char not in stack:
            while stack and stack[-1] in s[i:] and char < stack[-1]:
                stack.pop()
            
            stack.append(char)

    return ''.join(stack)
