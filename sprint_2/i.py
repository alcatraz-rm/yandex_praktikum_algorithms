
class MyQueueSized:
    def __init__(self, max_size):
        self._max_size = max_size
        self._size = 0
        self._head = 0
        self._tail = 0
        self._data = [None] * max_size

    def push_back(self, x):
        if self._size == self._max_size:
            print('error')
            return
        self._data[self._tail] = x
        self._tail = (self._tail + 1) % self._max_size
        self._size += 1

    def pop_front(self):
        if self._size == 0:
            print('error')
            return
        result = self._data[self._head]
        self._data[self._head] = None
        self._head = (self._head + 1) % self._max_size
        self._size -= 1
        return result

    def peek(self):
        return self._data[self._head]

    def size(self):
        return self._size


n = int(input())
m = int(input())
queue = MyQueueSized(m)

for _ in range(n):
    command = input().split()
    match command[0]:
        case 'pop':
            print(queue.pop_front())
        case 'peek':
            print(queue.peek())
        case 'size':
            print(queue.size())
        case 'push':
            queue.push_back(int(command[1]))
