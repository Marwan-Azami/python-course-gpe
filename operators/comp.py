var_a = 5
var_b = 4
var_c = 20

print(" == ", var_a * var_b == var_c)
print(" > ", var_a > var_b)
print(" < ", var_a < var_b)
print(" != ", var_a != var_b)
print(" >= ", var_a >= var_a)

# == et =
tmp_1 = var_a = var_b
tmp_2 = var_a == var_b
print("**************************")
print("a == b", tmp_2)
print("a = b", tmp_1)
print("**************************")