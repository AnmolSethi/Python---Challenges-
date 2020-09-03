if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        students.append([name, score])
    if len(students) >= 2 and len(students) <= 5:
        scores = set([students[x][1] for x in range(len(students))])
        scores = list(scores)
        scores.sort()

        students = [x[0] for x in students if x[1] == scores[1]]
        for s in sorted(students):
            print(s)