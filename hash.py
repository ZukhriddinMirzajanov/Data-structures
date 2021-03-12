class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        for item in self.arr[h]:
            if item[0] == key:
                return item[1]

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        for index, item in enumerate(self.arr[h]):
            if len(item) == 2 and item[0] == key:
                self.arr[h][index] = [key, value]
                found = True
                break
        if not found:
            self.arr[h].append([key, value])

    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, item in enumerate(self.arr[h]):
            if item[0] == key:
                del self.arr[h][index]


hash_table = HashTable()
hash_table['room'] = 10
hash_table['room 6'] = 13
hash_table['room 17'] = 20
del hash_table['room 6']
print(hash_table.arr)
