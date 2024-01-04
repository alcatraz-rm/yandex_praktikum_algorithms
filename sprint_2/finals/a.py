
class Queue:
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

    def push_front(self, x):
        if self._size == self._max_size:
            print('error')
            return
        self._data[self._head - 1] = x
        self._head = (self._head - 1) % self._max_size
        self._size += 1

    def pop_back(self):
        if self._size == 0:
            print('error')
            return
        result = self._data[self._tail - 1]
        self._data[self._tail - 1] = None
        self._tail = (self._tail - 1) % self._max_size
        self._size -= 1
        return result

    def pop_front(self):
        if self._size == 0:
            print('error')
            return
        result = self._data[self._head]
        self._data[self._head] = None
        self._head = (self._head + 1) % self._max_size
        self._size -= 1
        return result


n = int(input())
m = int(input())
queue = Queue(m)

for _ in range(n):
    command = input().split()
    match command[0]:
        case 'pop_front':
            res = queue.pop_front()
            if res is not None:
                print(res)
        case 'pop_back':
            res = queue.pop_back()
            if res is not None:
                print(res)

        case 'push_back':
            queue.push_back(int(command[1]))
        case 'push_front':
            queue.push_front(int(command[1]))
