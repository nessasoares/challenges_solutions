def to_url(phrase):
    array = phrase.split()

    return '%20'.join(array)

print(to_url('vanessa santos soares'))