class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        self.m = 31
        self.map = [[] for _ in range(self.m)]

    def put(self, key: int, value: int) -> None:
        hash = self._hash(key)

        key_list = [data[0] for data in self.map[hash]]
        if key in key_list:
            key_idx = key_list.index(key)
            self.map[hash][key_idx] = (key, value)
        else:
            self.map[hash].append((key, value))

    def get(self, key: int) -> int:
        hash = self._hash(key)
        for data in self.map[hash]:
            if data[0] == key:
                return data[1]
        return -1

    def remove(self, key: int) -> None:
        hash = self._hash(key)
        for i, data in enumerate(self.map[hash]):
            if data[0] == key:
                self.map[hash].pop(i)
                break

    def _hash(self, key):
        return key % self.m
