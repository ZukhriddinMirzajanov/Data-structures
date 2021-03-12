class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()

    def iterate(self):
        if self.LinkedList.head is None:
            print('The queue is empty')
        else:
            node = self.LinkedList.head
            while node:
                print(node.value)
                node = node.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.LinkedList.head is None:
            self.LinkedList.head = new_node
            self.LinkedList.tail = new_node
        else:
            self.LinkedList.tail.next = new_node
            self.LinkedList.tail = new_node

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False

    def dequeue(self):
        if self.isEmpty():
            return 'The queue is empty'
        else:
            temp_node = self.LinkedList.head
            if self.LinkedList.head == self.LinkedList.tail:
                self.LinkedList.head = None
                self.LinkedList.tail = None
                return temp_node
            else:
                self.LinkedList.head = self.LinkedList.head.next
                return temp_node

    def peek(self):
        if self.isEmpty():
            print('The queue is empty')
        else:
            print(self.LinkedList.head.value)

    def delete(self):
        self.LinkedList.head = None
        self.LinkedList.tail = None
