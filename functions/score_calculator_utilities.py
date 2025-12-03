
# Define a function that asks the user to provide a input which we will
# return
def get_mark():
    grade = float(input("Please provide a mark: "))
    return grade

# This function asks the users if they want to continue
def ask_if_continue():
    response = input("Do you want to continue y = Yes, n = N")
    return response

# This function calculates the avg
def sum_of_tableau(tableau):
    _sum = 0 #
    for valeur  in tableau:
        _sum+= valeur
    return _sum

def avg_of_tableau(tableau):
    avg = sum_of_tableau(tableau) / len(tableau)
    return avg


# Ajouter une fonction qui permet de faire scoring