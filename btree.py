import queue


class BTree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def pre_order(self, root_node):
        if not root_node:
            return 'BT is not exist'
        print(root_node.data)
        self.pre_order(root_node.left_child)
        self.pre_order(root_node.right_child)

    def in_order(self, root_node):
        if not root_node:
            return 'BT is not exist'
        self.pre_order(root_node.left_child)
        print(root_node.data)
        self.pre_order(root_node.right_child)

    def post_order(self, root_node):
        if not root_node:
            return 'BT is not exist'
        self.pre_order(root_node.left_child)
        self.pre_order(root_node.right_child)
        print(root_node.data)

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
        if not root_node:
            return 'BT is not exist'
        else:
            costom_queue = queue.Queue()
            costom_queue.enqueue(root_node)
            while not costom_queue.isEmpty():
                root = costom_queue.dequeue()
                if root.value.data == node_value:
                    return node_value
                if root.value.left_child is not None:
                    costom_queue.enqueue(root.value.left_child)

                if root.value.right_child is not None:
                    costom_queue.enqueue(root.value.right_child)
            return 'Not Found'

    def insert(self, root_node, new_node_value):
        new_node = BTree(new_node_value)
        if not root_node:
            root_node = new_node
        else:
            costom_queue = queue.Queue()
            costom_queue.enqueue(root_node)
            while not costom_queue.isEmpty():
                root = costom_queue.dequeue()
                if root.value.left_child is not None:
                    costom_queue.enqueue(root.value.left_child)
                else:
                    root.value.left_child = new_node
                    return 'Inserted'
                if root.value.right_child is not None:
                    costom_queue.enqueue(root.value.right_child)
                else:
                    root.value.right_child = new_node
                    return 'Inserted'

    def get_deepest_node(self, root_node):
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
            return root.value

    def delete_deepest(self, root_node, dNode):
        if not root_node:
            return 'BT is not exist'
        else:
            costom_queue = queue.Queue()
            costom_queue.enqueue(root_node)
            while not costom_queue.isEmpty():
                root = costom_queue.dequeue()
                if root.value == dNode:
                    root.value = None
                    return
                if root.value.right_child:
                    if root.value.right_child is dNode:
                        root.value.right_child = None
                        return
                    else:
                        costom_queue.enqueue(root.value.right_child)
                if root.value.left_child:
                    if root.value.left_child is dNode:
                        root.value.left_child = None
                        return
                    else:
                        costom_queue.enqueue(root.value.left_child)

    def delete_node(self, root_node, node):
        if not root_node:
            return 'BT is not exist'
        else:
            costom_queue = queue.Queue()
            costom_queue.enqueue(root_node)
            while not costom_queue.isEmpty():
                root = costom_queue.dequeue()
                if root.value.data == node:
                    dNode = self.get_deepest_node(root_node)
                    root.value.data = dNode.data
                    self.delete_deepest(root_node, dNode)
                    return 'Deleted'
                if root.value.left_child is not None:
                    costom_queue.enqueue(root.value.left_child)

                if root.value.right_child is not None:
                    costom_queue.enqueue(root.value.right_child)

    def delete_bt(self, root_node):
        root_node.data = None
        root_node.left_child = None
        root_node.right_child = None
        return 'Deleted'


btree = BTree('Books')
left_child = BTree('Classics')
right_child = BTree('Fantasy')
btree.left_child = left_child
btree.right_child = right_child
btree.insert(btree, 'Ninth House')
print(btree.delete_bt(btree))
btree.level_order(btree)
