import queue


class Tree:
    def __init__(self, data, child=[]):
        self.data = data
        self.child = child

    def __str__(self, level=0):
        ret = '  '*level + str(self.data) + '\n'
        for child in self.child:
            ret += child.__str__(level + 1)
        return ret

    def add_child(self, Tree):
        self.child.append(Tree)


tree = Tree('Books', [])
classics = Tree('Classics', [])
detective = Tree('Detective', [])
fantasy = Tree('Fantasy', [])
tree.add_child(classics)
tree.add_child(fantasy)
tree.add_child(detective)
beloved = Tree('Beloved', [])
night_fire = Tree('The Night Fire', [])
ninth_house = Tree('Ninth House', [])
classics.add_child(beloved)
detective.add_child(night_fire)
fantasy.add_child(ninth_house)

print(tree)


def bs(array, data):
    left = 0
    right = len(array)-1
    while left <= right:
        mid = int((left + right)/2)
        if data == array[mid]:
            return array[mid]
        elif data < array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return 'data is not exist inside the array'


array = [1, 2, 3, 4, 5, 6]
print(bs(array, 0))
