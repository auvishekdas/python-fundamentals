num1 = set([12,14,16,17,18,20])
num1.add(22)
num1.remove(17)
print(num1)
print(22 in num1)
print(32 in num1)
print(14 not in num1)
print(38 not in num1)

num2 = {4,6,8,10,12}
num3 = {18,20,22,24,26}
print(num2 | num3)
print(num2 & num3)
print(num2 - num3)