
class List:
    class Node:
        def __init__(self, value, next_item):
            self._value = value
            self._next = next_item

        @property
        def value(self):
            return self._value

        @property
        def next(self):
            return self._next

        def set_next(self, item):
            self._next = item

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def push_back(self, x):
        if not self._head:
            self._head = self.Node(x, None)
            self._tail = self._head
        else:
            new_item = self.Node(x, None)
            self._tail.set_next(new_item)
            self._tail = new_item
        self._size += 1

    def pop_front(self):
        if self._size > 0:
            result = self._head.value
            self._head = self._head.next
            self._size -= 1
            return result

    def size(self):
        return self._size


class Queue:
    def __init__(self):
        self._data = List()

    def put(self, x):
        self._data.push_back(x)

    def get(self):
        return self._data.pop_front()

    def size(self):
        return self._data.size()


queue = Queue()

for _ in range(int(input())):
    command = input().split()
    match command[0]:
        case 'get':
            result = queue.get()
            print(result if result is not None else 'error')
        case 'size':
            print(queue.size())
        case 'put':
            queue.put(int(command[1]))
