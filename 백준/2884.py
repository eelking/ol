h, m = map(int, input().split())

h = (h + 24 - (m < 45)) % 24
m = (m + 15) % 60

print(h, m)

# h, m = map(int , input().split())

# if m >= 45:
#     print(h, m - 45)
# else:
#     if h == 0:
#         print(23, 15 + m)
#     else:
#         print(h - 1, 15 + m)