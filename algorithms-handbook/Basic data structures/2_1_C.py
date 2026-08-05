
"""
C. Первое вхождение числа в массив.

Сложность: O(n + q) по времени, O(n + q) по памяти.

Для каждого запроса x нужно вывести самую левую позицию x в массиве
или -1, если x не встречается.

Чтобы не проходить по массиву для каждого запроса, сначала строим словарь:
число -> его первая позиция. Затем ответы на запросы берем из словаря
и выводим все результаты в конце.
"""


n, q = map(int, input().split())
a = list(map(int, input().split()))
answer = []

first_positions = {}
for i in range(n):
    value = a[i]
    position = i + 1
    if value not in first_positions:
        first_positions[value] = position

for _ in range(q):
    x = int(input())
    if x in first_positions:
        answer.append(first_positions[x])
    else:
        answer.append(-1)

print(*answer, sep="\n")
