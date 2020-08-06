import pytest
from collections import Counter

def checkMagazine(magazine, notes):
    magazine_counter = Counter(magazine)
    notes_counter = Counter(notes)

    canWrite = notes_counter - magazine_counter

    result = 'Yes' if len(canWrite) == 0 else 'No'
    print(result)

    return result

class Test_Kidnapper():
    def test_examples(self):

        magazine = 'give me one grand today night'
        note = 'give one grand today'

        assert 'Yes' == checkMagazine(magazine, note)

        magazine = 'two times three is not four'
        note = 'two times two is four'

        assert 'No' == checkMagazine(magazine, note)

        magazine = 'ive got a lovely bunch of coconuts'
        note = 'ive got some coconuts'

        assert 'No' == checkMagazine(magazine, note)