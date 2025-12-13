ma_list = [1, 3, 0, 10]

# 0 -> 1
# 1 -> 3
# 2 -> 0
# 3 -> 10 len -1 (4)

# max_index = len(ma_list) -1
# print(ma_list[max_index])

# for index, x in enumerate(ma_list):
#     print("index = ", index)
#     print("x = ", x)
     #print(ma_list[len(ma_list)-index-1])
def my_reverse(ma_list):
    reverse_list = []
    index = 0
    for x in ma_list:
        #print("index = ", index)
        #print("x = ", x)
        reverse_list.append(ma_list[len(ma_list) - 1 - index])
        index +=1
    return reverse_list


print(my_reverse(ma_list))
print(my_reverse(['a','b', 'c', 'd', 'e']))