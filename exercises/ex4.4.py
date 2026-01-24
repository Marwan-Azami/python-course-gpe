
ma_list = [7, 5, 11, 2, 10, 9, 16]
index = 0
while index < len(ma_list)- 2:
    current_value = ma_list[index]
    next_value   = ma_list[index+1]
    if current_value > next_value:
        ma_list[index] = next_value
        ma_list[index+1] = current_value
        index = 0
        continue
    index+=1
print(ma_list)