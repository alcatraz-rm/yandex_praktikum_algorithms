
class StackMaxEffective:
    def __init__(self):
        self._data = []
        self._max_elements = []
        self._max = None
        self._size = 0

    def push(self, value):
        if self._max is None:
            self._max = value
            self._max_elements.append(value)
        elif value >= self._max:
            self._max = value
            self._max_elements.append(value)
        self._data.append(value)
        self._size += 1

    def top(self):
        if self._size > 0:
            return self._data[-1]

    def pop(self):
        if self._size > 0:
            need_to_update_max = (self._data[-1] == self._max)
            del self._data[-1]
            self._size -= 1

            if need_to_update_max:
                del self._max_elements[-1]
                if self._size > 0:
                    self._max = self._max_elements[-1]
                else:
                    self._max = None
        else:
            print('error')

    def get_max(self):
        return self._max


stack = StackMaxEffective()

for _ in range(int(input())):
    command = input().split()
    match command[0]:
        case 'pop':
            stack.pop()
        case 'top':
            top = stack.top()
            print(top if top is not None else 'error')
        case 'get_max':
            print(stack.get_max())
        case 'push':
            stack.push(int(command[1]))
