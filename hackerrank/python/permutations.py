# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

word, size = input().split()

perms = sorted(permutations(list(word), int(size)))

for i in perms:
    print(''.join(i))