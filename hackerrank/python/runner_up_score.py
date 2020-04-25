if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    s = set(arr)
    list = list(s)
    list.sort()
    print(list[-2])