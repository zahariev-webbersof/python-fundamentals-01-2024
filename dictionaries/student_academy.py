n = int(input())
students = {}

for _ in range(n):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = []

    students[name].append(grade)

students_above_average = {name: sum(grades) / len(grades) for name, grades in students.items()
                          if sum(grades) / len(grades) >= 4.50}

for name, average_grade in students_above_average.items():
    print(f'{name} -> {average_grade:.2f}')
