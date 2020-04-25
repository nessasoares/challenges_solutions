if __name__ == '__main__':

    s = set()
    dict = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score not in dict.keys():
            dict[score] = [] 
        dict[score].append(name)

    import ipdb; ipdb.set_trace()

    sorted_dict = sorted(dict)
    second_slowest = sorted_dict[1]

    for student in sorted(dict[second_slowest]):
        print(student)