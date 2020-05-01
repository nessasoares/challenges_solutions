def count_substring(string, sub_string):
    subs_size = len(sub_string)
    i = 0
    keep_going = True
    counter = 0

    while keep_going:
        j = i + subs_size
        if j > len(string):
            break
        s = string[i:j]
        if s == sub_string:
            counter += 1
        i += 1
    return counter



if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
