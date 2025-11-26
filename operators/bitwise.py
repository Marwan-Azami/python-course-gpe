# Bitwise operate at the binary level

a = 10
b = 3

# a = 1010
# b = 11
# 0 & 0 = 0
# 1 & 0 = 0
# 0 & 1 = 0
# 1 & 1 = 1
c = a & b
print(c)

# Or ou
# 0 ou 0 = 0
# 1 ou 0 = 1
# 0 ou 1 = 1
# 1 ou 1 = 1
c2 = a | b

print(c2)
print(bin(c2))

xor = a ^ b
print(xor)

shift_a = a >> 2  # 1010 => 10
shift_one = 1 << 5  # 100000
print(shift_a)
print(shift_one)