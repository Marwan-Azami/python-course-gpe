
def afficher_contenu_tab(tab):
    print("--"*10)
    for v in tab:
        print(v)
    print("--" * 10)

##
tab = []
tab.append("Hello") # add a value in the array
tab.append("GPE")
afficher_contenu_tab(tab)
tab.insert(0, "Salam")
afficher_contenu_tab(tab)
tab.pop(1) # remove an element with an index
afficher_contenu_tab(tab)
tab.append("GPE")
print(tab.count("GPE"))
afficher_contenu_tab(tab)
# print("Before deletion ")
# tab.remove("Hello") # delete the value from the array
# afficher_contenu_tab(tab)
#
# tab.append("New")
# afficher_contenu_tab(tab)
# tab.clear()
# print("(-_")
# afficher_contenu_tab(tab)
# print("(-_")