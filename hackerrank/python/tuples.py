if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tup = ()
    for i in integer_list:
        num = int(i)
        tup = tup + (num,)
    
    print(hash(tup))