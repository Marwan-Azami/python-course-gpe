
temp = int(input("Can you provide the water temperature please ?"))

print("Temperature = ", temp)
list_temp = [20, 40, 60, 80]
# [0-100]
if temp >=0 and temp <=100:
    print("Normal")
    if temp in list_temp: # to test if the temp is in the list
        print("In the list :", temp)

    if temp <= 20:
        print("<=20")
        if temp == 0:
            print("Zero....")
    elif temp > 20 and temp <= 40:
        print("Between 20 and 40")
    elif temp > 40 and temp <= 60:
        print(" Between 40 and 60")
    elif temp > 60 and temp <=80:
        print("Between 60 and 80")
    elif temp > 80 and temp <= 100:
        print("Between 80 and 100")
        if temp == 100:
            print("100 ....")
    # else:
    #     print(" Entre 80 and 100")
# -oo, 0[
elif temp < 0:
    print("low")
# 100, +oo
elif temp > 100:
    print("high")
else:
    print("Autre")