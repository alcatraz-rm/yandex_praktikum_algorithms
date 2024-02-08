
class HashMap:
    def __init__(self):
        self._hash_function = hash
        self._capacity = 10 ** 5
        self._data = [[] for _ in range(self._capacity)]

    def put(self, key: int, value: int):
        index = self._hash_function(key) % self._capacity
        for i, item in enumerate(self._data[index]):
            k = item[0]
            if k == key:
                self._data[index][i] = (k, value)
                return
        self._data[index].append((key, value))

    def get(self, key: int) -> int | None:
        index = self._hash_function(key) % self._capacity
        for item in self._data[index]:
            k, v = item
            if k == key:
                return v

    def delete(self, key: int) -> int | None:
        index = self._hash_function(key) % self._capacity
        for i, item in enumerate(self._data[index]):
            k, v = item
            if k == key:
                del self._data[index][i]
                return v


n = int(input())
hash_map = HashMap()

for _ in range(n):
    query, *args = input().split()
    key = int(args[0])

    match query:
        case 'get':
            print(hash_map.get(key))
        case 'put':
            value = int(args[1])
            hash_map.put(key, value)
        case 'delete':
            print(hash_map.delete(key))
