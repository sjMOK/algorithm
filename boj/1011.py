def solution(x, y):
    if y - x <= 2:
        return y - x
    
    cnt = 2
    x, y = x + 1, y -1
    window = 1
    while x < y:
        between = y - x
        next_window = window + 1
        
        if between <= next_window:
            x += max(between, next_window)
            cnt += 1
        elif between < next_window * 2:
            x += next_window
            y -= between - next_window
            cnt += 2
        else:
            x += next_window
            y -= next_window
            cnt += 2
        
        window += 1
    return cnt

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    print(solution(x, y))
