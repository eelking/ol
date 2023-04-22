h, m = map(int, input().split())
t = int(input())

h = (h + (t // 60) + (t % 60 + m >= 60)) % 24
m = (m + (t % 60)) % 60

print(h, m)

# d = 60 * 24 + h * 60 + m + t
# print(d // 60 % 24, d % 60)