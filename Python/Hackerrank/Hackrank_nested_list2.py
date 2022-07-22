python_students = []
for user_input in range(5):
    name = input()
    score = float(input())
    python_students.append([score, name])

python_students.sort()

print('lowest score', python_students[0])
lowest = python_students[0]
for rank in python_students:
    if rank[0] > lowest[0]:
        print(rank[1])
        break
secondlowest = rank
print('secondlowest:', secondlowest)
for equalrank in python_students:
    if equalrank[0] == secondlowest[0] and equalrank[1] > secondlowest[1]:
        print(equalrank[1])

# You can do this with "destructuring" look it up (Python, Javascripts etc...)

print(python_students)
