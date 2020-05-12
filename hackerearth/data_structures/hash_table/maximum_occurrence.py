string = input()

table = {}
higher = 0 
letter = ''

for char in string:
    if char not in table.keys():
        table[char] = 1
    else:
        table[char] +=1

    if table[char] > higher:
        higher = table[char]

sorted_table = {k: v for k, v in sorted(table.items(), key=lambda item: item[0]) if v == higher}

for k, v in sorted_table.items():
    print(str(k) + " " + str(v))
    break