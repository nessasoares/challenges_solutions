keep_going = True
index = 0
while keep_going:
    try:
        if index == 12:
            break
        input_ = input()
    except EOFError:
        break
    a, b = input_.split()
    sum = int(a) + int(b)
    print(sum)
    index += 1
