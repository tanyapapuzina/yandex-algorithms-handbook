
"""
B. Поиск пар индексов для минимальной и максимальной разности.

Сложность: O(n) по времени, O(1) по памяти.

Нужно найти две пары индексов i < j:

- пару, где a[i] - a[j] минимально;
- пару, где a[i] - a[j] максимально.

Перебирать все пары нельзя: при большом n это даст O(n^2) и приведет
к превышению лимита времени. Поэтому решение идет по массиву один раз.

Идея:

Когда мы стоим на текущем элементе a[j], все элементы слева от него уже
могут быть первым элементом пары. Для минимальной разности нужно знать
самое маленькое значение слева, а для максимальной разности - самое большое
значение слева.

На каждом шаге:

1. Считаем кандидата на минимум: min_value - a[j].
2. Считаем кандидата на максимум: max_value - a[j].
3. Если кандидат лучше текущего ответа, обновляем ответ и индексы.
4. После этого обновляем min_value и max_value текущим элементом,
   чтобы он мог участвовать как левый элемент в следующих парах.

"""

n = int(input())
a = list(map(int, input().split()))

def max_min(a):
    n = len(a)

    min_value = a[0] #Самое маленькое число слева от текущей позиции
    min_value_index = 1

    max_value = a[0] #Самое большое число слева от текущей позиции
    max_value_index = 1

    min_diff = a[0] - a[1]
    min_i = 1
    min_j = 2

    max_diff = a[0] - a[1]
    max_i = 1
    max_j = 2

    for j in range(1, n):
        
        if min_diff > min_value - a[j]:
            min_diff = min_value - a[j]
            min_i = min_value_index
            min_j = j + 1

        if max_diff < max_value - a[j]:
            max_diff = max_value - a[j]
            max_i = max_value_index
            max_j = j + 1

        if a[j] < min_value:
            min_value = a[j]
            min_value_index = j + 1
        
        if a[j] > max_value:
            max_value = a[j]
            max_value_index = j + 1

    print(min_i, min_j)
    print(max_i, max_j)

max_min(a)
