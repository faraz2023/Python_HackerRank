students = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    students.append([name, score])
second_lowest=sorted(list(set([x[1] for x in students])))[1]
second_students=sorted([s for s,g in students if g==second_lowest])
for s in second_students:
    print(s)
