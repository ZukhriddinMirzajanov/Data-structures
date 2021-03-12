class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def iterate(self):
        if self.head is None:
            print('The list is not exist')
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next

    def reverse_iterate(self):
        if self.head is None:
            print('The list is not exist')
        else:
            node = self.tail
            while node:
                print(node.value)
                node = node.prev

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            new_node.prev = None
            new_node.next = None
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = None
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert(self, value, index):
        new_node = Node(value)
        if self.head is None:
            new_node.prev = None
            new_node.next = None
            self.head = new_node
            self.tail = new_node
        else:
            if index == 0:
                new_node.prev = None
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            else:
                temp_node = self.head
                itr_count = 0
                while itr_count < index - 1:
                    temp_node = temp_node.next
                    itr_count += 1
                new_node.next = temp_node.next
                new_node.prev = temp_node
                new_node.next.prev = new_node
                temp_node.next = new_node

    def search(self, node_value):
        if self.head is None:
            print('The list is not exist')
        else:
            node = self.head
            while node:
                if node.value == node_value:
                    return node.value
                node = node.next
            return 'The value is not exist in the list'

    def pop(self):
        if self.head is None:
            print('The list is not exist')
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None

    def delete_node(self, index):
        if self.head is None:
            print('The list is not exist')
        else:
            if index == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            else:
                temp_node = self.head
                itr_count = 0
                while itr_count < index - 1:
                    temp_node = temp_node.next
                    itr_count += 1
                temp_node.next = temp_node.next.next
                temp_node.next.prev = temp_node

    def delete_list(self):
        if self.head is None:
            print('The list is not exist')
        else:
            temp_node = self.head
            while temp_node:
                temp_node.prev = None
                temp_node = temp_node.next
            self.head = None
            self.tail = None


doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append(0)
doubly_linked_list.append(1)
doubly_linked_list.append(2)
doubly_linked_list.append(3)
doubly_linked_list.append(4)
doubly_linked_list.insert(8, 3)
doubly_linked_list.delete_list()
doubly_linked_list.iterate()
