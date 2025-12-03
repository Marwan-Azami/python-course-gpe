
sum_grades = 0
sum_grades2 = 0
sum_grades3 = 0

grades = [12, 13, 10]
grades2 = [10, 13, 20]
grades3 = [12, 13, 10]
# Summation
for grade in grades:
    # block
    # Sigma des notes
    sum_grades = sum_grades + grade

print("sum_grades = ", sum_grades)
# Dividing the sum over the number of grades
avg_grades = sum_grades / len(grades)


for grade in grades2:
    # block
    # Sigma des notes
    sum_grades2 = sum_grades + grade

print("sum_grades = ", sum_grades)
# Dividing the sum over the number of grades
avg_grades2 = sum_grades / len(grades)