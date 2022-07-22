n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    # scores = [float(x) for x in line]
    student_marks[name] = scores
query_name = input()


floataverage = sum(student_marks[query_name])/len(student_marks[query_name])
formatavarage = "{:.2f}".format(floataverage)
print(formatavarage)
