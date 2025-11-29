
sum_of = 0
# 1 - 2
# 2 - 4
# 3 - 5
for y in [5, 4, 2, 1]:
    print("The current value of y = ", y )
    sum_of = sum_of + y # 1) y  = 5, sum_of -> 0, sum_of = 5
                        # 2) y = 4, sum_of -> 5, sum_of = 4 + 5
                        # 3) y = 2, sum_of -> 9, sum_of= 9 + 2
                        # 4) y = 1, sum_of -> 11, sum_of = 12
    print("Sum of = ", sum_of)