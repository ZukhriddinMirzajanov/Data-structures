import queue


class BSTree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert(self, root_node, node_value):
        if root_node.data is None:
            root_node.data = node_value
        elif node_value <= root_node.data:
            if root_node.left_child is None:
                root_node.left_child = BSTree(node_value)
            else:
                self.insert(root_node.left_child, node_value)
        else:
            if root_node.right_child is None:
                root_node.right_child = BSTree(node_value)
            else:
                self.insert(root_node.right_child, node_value)
        return 'Inserted'

    def level_order(self, root_node):
        if not root_node:
            return 'BT is not exist'
        else:
            costom_queue = queue.Queue()
            costom_queue.enqueue(root_node)
            while not costom_queue.isEmpty():
                root = costom_queue.dequeue()
                print(root.value.data)
                if root.value.left_child is not None:
                    costom_queue.enqueue(root.value.left_child)

                if root.value.right_child is not None:
                    costom_queue.enqueue(root.value.right_child)

    def search(self, root_node, node_value):
        if root_node.data == node_value:
            return 'Found'
        elif node_value < root_node.data:
            if root_node.left_child.data == node_value:
                return 'Found'
            else:
                self.search(root_node.left_child, node_value)
        else:
            if root_node.right_child.data == node_value:
                return 'Found'
            else:
                self.search(root_node.right_child, node_value)

    def min_node_value(self, root_node):
        node = root_node
        while node.left_child is not None:
            node = node.left_child
        return node

    def delete_node(self, root_node, node_value):
        if root_node is None:
            return root_node
        if node_value < root_node.data:
            root_node.left_child = self.delete_node(
                root_node.left_child, node_value)
        elif node_value > root_node.data:
            root_node.right_child = self.delete_node(
                root_node.right_child, node_value)
        else:
            if root_node.left_child is None:
                temp = root_node.right_child
                root_node = None
                return temp
            if root_node.right_child is None:
                temp = root_node.left_child
                root_node = None
                return temp
            temp = self.min_node_value(root_node.right_child)
            root_node.data = temp.data
            root_node.right_child = self.delete_node(
                root_node.right_child, temp.data)
        return root_node

    def delete_bst(self, root_node):
        root_node.data = None
        root_node.left_child = None
        root_node.right_child = None
        return 'BST is deleted'


bstree = BSTree(None)
bstree.insert(bstree, 60)
bstree.insert(bstree, 90)
bstree.insert(bstree, 30)
bstree.delete_bst(bstree)
bstree.level_order(bstree)
