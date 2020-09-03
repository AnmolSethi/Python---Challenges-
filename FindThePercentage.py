if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks.keys():
        avg_scores = list()
    for i in student_marks.pop(query_name):
        avg_scores.append(i)
    print('{0:.2f}'.format(sum(avg_scores) / 3))