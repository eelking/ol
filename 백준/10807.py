input()
l = list(map(int, input().split()))
t = int(input())

count = 0
for i in l:
    if t == i:
        count += 1

print(count)

# input()
# print(list(map(int, input().split())).count(int(input())))