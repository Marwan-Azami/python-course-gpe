tab = [
        [1, 2, 3],
        [3, 2, 3],
        [ # 3
            [1, 4],
            [2, 4, 7],
            [4]
        ]
       ]
#print(tab[2][2])
# x, y 2
print(tab[2][1][2])
#tab = [1, 2, 3]
for x in tab: # Iter 0
#for index, x in enumerate(tab):  # Iter 0
    #print("index ", index)
    print(x)
    for y in x:
        #print(y)
        if type(y) == list:
            for z in y:
                print(z)


