a, t = map(int, input().split())
l = list(map(int, input().split()))

for i in l:
    if t > i:
        print(i, end=' ')