
"""
2.1 Singly linked list / Односвязный список.

В этом файле реализована простая учебная версия односвязного списка.
Односвязный список состоит из узлов. Каждый узел хранит значение и ссылку
на следующий узел. Сам список хранит ссылку на первый узел - head.

Что реализовано:

- Node - один узел списка:
  - value хранит значение;
  - next хранит ссылку на следующий узел.

- SinglyLinkedList - сам список:
  - push_front(value) добавляет элемент в начало;
  - push_back(value) добавляет элемент в конец;
  - pop_front() удаляет первый элемент;
  - find(value) ищет значение и печатает YES или NO;
  - to_list() превращает связный список в обычный Python-список;
  - print_all() печатает элементы по одному, использовался для отладки.

Программа читает команды из терминала:

push_front x - добавить x в начало списка;
push_back x - добавить x в конец списка;
pop_front - удалить первый элемент;
find x - проверить, есть ли x в списке;
print - вывести список в одну строку или EMPTY, если список пустой.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def print_all(self):
        current = self.head

        while current is not None:
            print(current.value)
            current = current.next

    def push_back(self, value):
        new_node = Node(value)
        current = self.head

        if current is None:
            self.head = new_node

        else:
            while current.next is not None:
                current = current.next
            current.next = new_node

    def pop_front(self):
        if self.head is None:
            return

        self.head = self.head.next

    def find(self, value):

        current = self.head

        while current is not None:
            if current.value == value:
                print("YES")
                return
            current = current.next

        print("NO")

    def to_list(self):
        list = []
        current = self.head

        while current is not None:
            list.append(current.value)
            current = current.next

        return list

linked_list = SinglyLinkedList()

n = int(input())

print("\nOutput:")

for _ in range(n):
    command = input().split()

    if command[0] == "push_front":
        value = int(command[1])
        linked_list.push_front(value)

    elif command[0] == "push_back":
        value = int(command[1])
        linked_list.push_back(value)

    elif command[0] == "pop_front":
        linked_list.pop_front()

    elif command[0] == "find":
        value = int(command[1])
        linked_list.find(value)

    elif command[0] == "print":
        values = linked_list.to_list()

        if len(values) == 0:
            print("EMPTY")
        else:
            print(*values)
