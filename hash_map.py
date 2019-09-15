# Simple hash map using list
class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashMap:
    def __init__(self, size):
        self.size = size
        self.data = [[] for _ in range(size)]

    def _hash_func(self, key):
        return key % self.size

    def display(self):
        for index in range(self.size):
            print('{} --> {}'.format(index, [item.value for item in self.data[index]]))

    def set(self, key, value):
        hash_index = self._hash_func(key)
        for item in self.data[hash_index]:
            if item.key == key:
                item.value = value
                return
        self.data[hash_index].append(Item(key, value))

    def get(self, key):
        hash_index = self._hash_func(key)
        for item in self.data[hash_index]:
            if item.key == key:
                return item.value
        raise KeyError('Key {} not Found'.format(key))

    def remove(self, key):
        hash_index = self._hash_func(key)
        for index, item in enumerate(self.data[hash_index]):
            if item.key == key:
                del self.data[hash_index][index]
                return
        raise KeyError('Key {} not Found'.format(key))

hash_map = HashMap(4)
hash_map.set(2,2)
hash_map.set(3,3)
hash_map.set(4,4)
hash_map.set(5,5)
hash_map.set(6,6)
hash_map.set(7,7)
hash_map.set(8,8)
hash_map.set(9,9)

print('Initial Hash Map')
hash_map.display()

hash_map.set(8, 16)
hash_map.set(3, 13)

print('\nModified Hash Map')
hash_map.display()


hash_map.remove(6)
#hash_map.remove(6) -- KeyError should come
print('\nAfter removing 6')
hash_map.display()
