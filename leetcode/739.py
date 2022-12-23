def daily_temperature(temperatures):
    answer = [0 for _ in temperatures]
    stack = []

    for i, temperature in enumerate(temperatures):
        while stack and temperature > temperatures[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last

        stack.append(i)

    return answer
