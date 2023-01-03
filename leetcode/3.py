def length_of_longest_substring(s):
    substring = ''
    length = 0
    for char in s:
        if char in substring:
            substring = substring[substring.index(char) + 1:]
        else:
            length = max(length, len(substring) + 1)

        substring += char

    return length

print(length_of_longest_substring('pwwkew'))