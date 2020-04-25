N = int(input())

vowels = {"a", "e", "i", "o", "u"}

for k in range(N):
    str_ = input()

    subs = [str_[i: j] for i in range(len(str_))
              for j in range(i + 1, len(str_) + 1)
              if any(char in vowels for char in str_[i: j])]
    counter = 0
    for s in subs:
        s = s.lower()
        for v in vowels:
            if v in s:
                counter += s.count(v)

    print(counter)
