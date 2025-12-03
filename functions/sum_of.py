
# Table [1, 2, 3] -> 6
# input -> return -> sum
# # Table [3, 3, 4] -> 10

def sum_of_tableau(tableau):
    _sum = 0 #
    for valeur  in tableau:
        _sum+= valeur
    return _sum

tab = [11, 12, 13]

#[
# --------
# --------
# --------
# ]
tab = [
           [11, 12, 14, 20, 19, 20, 15],
           [11, 10, 14, 20, 19, 20, 15],
           [11, 12, 14, 10, 10, 20, 15]
       ]


tab1 = []
tab2 = []
tab3
#print(sum_of_tableau(tab))  # calling the function # print the result
#print(sum_of_tableau(tab2))

for row in tab:
    print(row)
    print(sum_of_tableau(row))
