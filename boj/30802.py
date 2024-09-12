def main():
    n = int(input())
    t_nums = list(map(int, input().split()))
    t, p = map(int, input().split())

    t_cnt = 0
    for num in t_nums:
        t_cnt += num // t
        t_cnt += 1 if num % t > 0 else 0
        
    print(t_cnt)
    print(n // p, n % p)


if __name__ == '__main__':
    main()
