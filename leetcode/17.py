def letter_combinations(digits):
    mapping = {
        '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z'],
    }

    def get_combinations(digits, combinations=[]):
        if not digits:
            return combinations

        if not combinations:
            combinations.append('')

        digit = digits[0]
        ret = []

        for comb in combinations:
            for letter in mapping[digit]:
                ret.append(comb + letter)

        combinations = get_combinations(digits[1:], ret)
        return combinations

    return get_combinations(digits)

print(letter_combinations('1'))