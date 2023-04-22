a = int(input())
b = int(input())
c = a * b

print(a * (b % 10))
b = b // 10
print(a * (b % 10))
b = b // 10
print(a * (b % 10))
print(c)

# a = int(input())
# b = input()

# print(a * int(b[2]))
# print(a * int(b[1]))
# print(a * int(b[0]))
# print(a * int(b))