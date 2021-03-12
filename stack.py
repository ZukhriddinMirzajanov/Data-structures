import queue


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def iterate(self):
        if self.LinkedList.head is None:
            print('The stack is empty')
        else:
            node = self.LinkedList.head
            while node:
                print(node.value)
                node = node.next

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.LinkedList.head
        self.LinkedList.head = new_node

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False

    def pop(self):
        if self.isEmpty():
            print('The stack is empty')
        else:
            node_value = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return node_value

    def peek(self):
        if self.isEmpty():
            print('The stack is empty')
        else:
            node_value = self.LinkedList.head.value
            return node_value

    def delete(self):
        self.LinkedList.head = None


stack = Stack()
print(stack.isEmpty())
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.peek())
stack.delete()
print("--")
stack.iterate()
