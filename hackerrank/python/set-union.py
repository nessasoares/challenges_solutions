import pytest

class Students():
    def __init__(self):
        self.english = {}
        self.french = {}

    def addStudents(self, subject, students):
        if subject == 'french':
            self.french = set(students)
        else:
            self.english = set(students)

    def countTotalSubscribed(self): 
        union = self.english.union(self.french)
        return len(union)


class TestDifference():
    def test_union(self):
        students = Students()

        eng = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        fr = [10, 1, 2, 3, 11, 21, 55, 6, 8]

        students.addStudents('french', fr)
        students.addStudents('english', eng)

        assert 13 == students.countTotalSubscribed()

if __name__ == '__main__':
    eng_students_size = int(input())
    eng_students = list(input().split())

    fr_students_size = int(input())
    fr_students = list(input().split())

    students = Students()

    students.addStudents('french', fr_students)
    students.addStudents('english', eng_students)

    print(students.countTotalSubscribed())