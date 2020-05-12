N = int(input())

students = {}
for i in range(N):
    student = input()
    if student not in students.keys():
        students[student] = 1
    else:
        students[student] += 1

sorted_students = {k: v for k, v in sorted(students.items(), key=lambda item: item[0])}

for k,v in sorted_students.items():
    print("{} {}".format(k, str(v))) 