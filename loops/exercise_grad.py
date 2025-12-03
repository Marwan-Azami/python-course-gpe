# Write a program that takes 10 grades found
# In a list, calculate the avg
# Gives a notation
# If the notation is between [0-9] Bad
# If the notation is between [10-20] Good
# Else print an error

list_notes = [13, 8, 19, 20, 14, 12, 7, 15, 12, 14] # Liste des notes
avg_grades = 0 # Moyenne des notes
sum_grades = 0
# The for loop
# Summation
for grade in list_notes:
    # block
    # Sigma des notes
    sum_grades = sum_grades + grade

print("sum_grades = ", sum_grades)
# Dividing the sum over the number of grades
avg_grades = sum_grades / len(list_notes)

print("Avg = ", avg_grades)
if avg_grades >= 0 and avg_grades < 10:
    print("Bad")
elif avg_grades >= 10 and avg_grades <= 20:
    print("Good")
    if avg_grades == 20:
        print("Very Very Good ...^_^")
else:
    print("Error")




