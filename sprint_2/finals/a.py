"""
https://contest.yandex.ru/contest/22781/run-report/104746258/

-- ПРИНЦИП РАБОТЫ --
Дек инициализируется с максимальным размером и массивом этого размера, заполненным значениями None.
Указатели head и tail, изначально равные 0, используются для отслеживания начала и конца Дека.

push_back(x): Этот метод добавляет элемент x в конец Дека.
Если Дек полон, он выводит сообщение об ошибке. В противном случае он помещает элемент в позицию, указываемую tail,
увеличивает tail (возвращаясь к началу, если необходимо), и увеличивает размер Дека.

push_front(x): Этот метод добавляет элемент x в начало Дека.
Он работает аналогично push_back(x), но уменьшает head, а не увеличивает tail.

pop_back(): Этот метод удаляет элемент из конца Дека.
Если Дек пуст, он выводит сообщение об ошибке. В противном случае он извлекает элемент из позиции перед tail,
устанавливает эту позицию в None, уменьшает tail (возвращаясь к началу, если необходимо),
и уменьшает размер Дека.

pop_front(): Этот метод удаляет элемент из начала Дека. Он работает аналогично pop_back(),
но увеличивает head, а не уменьшает tail.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Программа должна работать корректно, если входные команды являются допустимыми.
Кольцевой буфер позволяет эффективно использовать память, а указатели head и tail гарантируют,
что элементы добавляются и удаляются в правильном порядке.
Поле size предотвращает переполнение,
проверяя, полон ли Дек или пуст, перед добавлением или удалением элементов.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Временная сложность каждой операции (push_back(x), push_front(x), pop_back(), pop_front()) составляет O(1),
поскольку каждая операция включает в себя постоянное количество работы: обновление элемента массива и увеличение
или уменьшение указателя и поля size.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Пространственная сложность Дека составляет O(n), где n - максимальный размер Дека.
Это связано с тем, что Дек использует массив размера max_size для хранения своих элементов,
и несколько дополнительных переменных для отслеживания своего состояния.
Размер этих переменных не зависит от размера Дека, поэтому они не меняют асимптотику.
"""


class Deque:
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
        if not self._size:
            print('error')
            return
        result = self._data[self._tail - 1]
        self._data[self._tail - 1] = None
        self._tail = (self._tail - 1) % self._max_size
        self._size -= 1
        return result

    def pop_front(self):
        if not self._size:
            print('error')
            return
        result = self._data[self._head]
        self._data[self._head] = None
        self._head = (self._head + 1) % self._max_size
        self._size -= 1
        return result


n = int(input())
m = int(input())
deque = Deque(m)

for _ in range(n):
    command = input().split()
    match command[0]:
        case 'pop_front':
            res = deque.pop_front()
            if res is not None:
                print(res)
        case 'pop_back':
            res = deque.pop_back()
            if res is not None:
                print(res)

        case 'push_back':
            deque.push_back(int(command[1]))
        case 'push_front':
            deque.push_front(int(command[1]))
