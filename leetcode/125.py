def is_palindrome(s):
    converted_s = []
    for char in s:
        if char.isalnum():
            converted_s.append(char.lower())

    i = 0
    while i < len(converted_s) // 2:
        if converted_s[i] != converted_s[len(converted_s) - 1 - i]:
            return False

        i += 1

    return True
