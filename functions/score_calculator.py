from score_calculator_utilities import avg_of_tableau, get_mark, ask_if_continue
import random
#############################################
tab = []
while True:
    #m = get_mark() # the returned mark
    m = random.randint(0, 20)
    print("m = ", m)
    tab.append(m)
    resp = ask_if_continue() # y, n
    if resp == 'n':
        break
#############################################
print(tab)
print(avg_of_tableau(tab))