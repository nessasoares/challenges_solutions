def is_unique(word):
    dict = {}

    for letter in word:
        if letter in dict.keys():
            return False
        else:
            dict[letter] = 1
    return True

print(is_unique('abc'))
print(is_unique('vanessa'))
print(is_unique('qwertyuiopasdfghjklçzxcvb'))
print(is_unique('insconstitucionalissimamente'))
print(is_unique('qppolfjk'))
print(is_unique('soares'))