if __name__ == '__main__':
    s = input()

    has_alphanum = False
    has_alpha = False
    has_digit = False
    has_lower = False
    has_upper = False

    for letter in s:
        if letter.isalnum() and not has_alphanum:
            has_alphanum = True

        if letter.isalpha() and not has_alpha:
            has_alpha = True

        if letter.isdigit() and not has_digit:
            has_digit = True

        if letter.islower() and not has_lower:
            has_lower = True

        if letter.isupper() and not has_upper:
            has_upper = True

    print(has_alphanum)
    print(has_alpha)
    print(has_digit)
    print(has_lower)
    print(has_upper)
