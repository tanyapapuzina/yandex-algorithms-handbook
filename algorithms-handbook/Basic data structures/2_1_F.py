

n = int(input())
a = list(map(int, input().split()))

max_a = max(a)

for i in range(len(a)-1, -1, -1):
    if a[i] == max_a:
        del a[i]
        break

print(*a)