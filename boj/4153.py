def main():
    while True:
        l, m, n = map(int, input().split())
        
        lst = [l, m, n]
        if lst == [0, 0, 0]:
            break

        lst.sort()
        if lst[2] ** 2 == lst[0] ** 2 + lst[1] ** 2:
            print('right')
        else:
            print('wrong')


if __name__ == '__main__':
    main()
