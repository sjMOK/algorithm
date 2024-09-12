def get_stars(n):
    if n == 1:
        return '*'
    
    stars = get_stars(n / 3)
    lines = stars.split('\n')
    res = ''
    for line in lines:
        res += line * 3 + '\n'
        
    for line in lines:
        res += line
        res += ' ' * len(line)
        res += line +'\n'
        
    for i, line in enumerate(lines):
        res += line * 3
        res += '\n' if i < len(lines) - 1 else ''
    
    return res

n = int(input())
print(get_stars(n))
