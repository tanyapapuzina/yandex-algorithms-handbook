



n = int(input())
a = list(map(int, input().split()))

answer = []
answer.append(a[0])

for i in range(1, n-1):
    if not (a[i-1] > a[i] < a[i+1]):
        answer.append(a[i])
        
answer.append(a[-1])

print(len(answer))
print(*answer)