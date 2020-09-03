from collections import namedtuple

N = int(input())
HEADERS = input().split()

Student = namedtuple('Student', '{0} {1} {2} {3}'.format(HEADERS[0], HEADERS[1], HEADERS[2], HEADERS[3]))

studentList = []

for _ in range(N):
    VALUES = input().split()
    studentList.append(Student(VALUES[0], VALUES[1], VALUES[2], VALUES[3])) 

totalMarks = 0
for i in studentList:
    totalMarks += int(i.MARKS)

print('{0:.2f}'.format(totalMarks / N)) 