from score_calculator_utilities import avg_of_tableau, get_mark, ask_if_continue
import random

# Ajouter une fonction qui permet de faire scoring
def score(avg):
    if avg >= 0 and avg < 10:
        return "Bad"
    elif avg >= 10 and avg <= 20:
        if avg == 20:
            return "Very Very Good ...^_^"
        return "Good"
    else:
        return "Error"

#############################################
tab = []
while True:
    m = get_mark() # the returned mark
    #m = random.randint(0, 20)
    print("m = ", m)
    tab.append(m)
    resp = ask_if_continue() # y, n
    if resp == 'n':
        break
#############################################
print(tab)
bablbalba = avg_of_tableau(tab)
print(bablbalba)
score = score(bablbalba)
print(score)


## Un class -> [note]
## plusieurs class
## [ [1, 2, 12, 15 ],
## # [10, 20, 11]
# ]