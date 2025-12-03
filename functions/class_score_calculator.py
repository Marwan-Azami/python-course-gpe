from functions.score_calculator_utilities import get_mark, ask_if_continue

tab = [] # tableau de notes
while True:
    # lire si on veux rajouter des notes d'une classe
    resp = input("Do you want to add a class marks")
    if resp == 'n':
        break

    tmp_tab = []
    while True:

        m = get_mark()  # the returned mark
        # m = random.randint(0, 20)
        print("m = ", m)
        tmp_tab.append(m)
        resp = ask_if_continue()  # y, n
        if resp == 'n':
            tab.append(tmp_tab)
            break

print(tab)