# A functon to convert decimal to binary

def decimal_to_binary(value): # value = 16
    converted_value = "" # 01010101010
    while value > 0:
        division = value // 2 # 16  division =  8 remainder = 0
        remainder = value % 2
        value = division
        converted_value = str(remainder) + converted_value
    return converted_value


print(decimal_to_binary(16)) # 1111
#print(decimal_to_binary(8)) # 1000
