import math

def merge_the_tools(string, k):
    n = len(string)
    split_size = math.ceil(n/k)
    if split_size == 0:
        split_size = 1
    #print(str(n) + ' ' + str(k) + ' '+  str(split_size))
    substrs = [string[i:i+k] for i in range(0, n, k)]
    #print(substrs)
    for subs in substrs:
        result = ''.join(list(dict.fromkeys(subs)))
        print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
