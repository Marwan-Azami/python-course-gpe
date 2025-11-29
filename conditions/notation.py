# Un ensemble de notes
# Faire la somme
# tester la moyenne si > 6 good, entre 5-6 moyen et < 5 Bad

notes_etudiants =  [12, 14, 15, 19, 11, 9, 13, 12, 17, 19, 20, 10, 13, 0, 0, 0, 0, 0, 0, 0, 1, 1]


somme = 0
for note in notes_etudiants:
    somme += note
else:
    print("Somme ", somme)

moyenne = somme / len(notes_etudiants)

print(f"Moyenne {moyenne:.3f}")
if moyenne > 6:
    print("Good")
elif moyenne >= 5 and moyenne <=6:
    print("Medium")
else:
    print("Bad")

