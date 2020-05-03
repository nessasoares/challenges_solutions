def print_formatted(number):
    for i in range(1,number+1):
        print('{0:d} {0:o} {0:X} {0:b}'.format(
                i, i, i, i))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
