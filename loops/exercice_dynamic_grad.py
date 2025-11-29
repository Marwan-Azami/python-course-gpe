# Write a program that ask the user to provide dynamically a number of grades
# The program asks users if they want to continue Yes/No
# If yes add again Else calculate the avg and give the notation


grades = [] # Empty
to_continue = True # Continue

while to_continue == True: # To test if the condition == true
    # collect the given grade
    grade = float(input("Please provide a grade: "))
    # ask the user to continue or stop
    response = input("Do you want to continue y = Yes, n = No")
    # If the user wants to leave
    if response == "n":
        to_continue = False
    # add to the list
    grades.append(grade)
    print("Grades = ", grades)

#***************** Calculating the notation ***************

avg_grades = 0 # Moyenne des notes
sum_grades = 0
# The for loop
# Summation
for grade in grades:
    # block
    # Sigma des notes
    sum_grades = sum_grades + grade

print("sum_grades = ", sum_grades)
# Dividing the sum over the number of grades
avg_grades = sum_grades / len(grades)

print("Avg = ", avg_grades)
if avg_grades >= 0 and avg_grades < 10:
    print("Bad")
elif avg_grades >= 10 and avg_grades <= 20:
    print("Good")
    if avg_grades == 20:
        print("Very Very Good ...^_^")
else:
    print("Error")
