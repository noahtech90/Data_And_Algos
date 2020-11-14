class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        return print(self.preorder_search(self.root, find_val))

    def print_tree(self):
        return print(self.preorder_print(self.root, []))

    def preorder_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False

    def preorder_print(self, start, traversal):
        if start:
            traversal.append(start.value)
            if not start.left or not start.right:
                return traversal
            else:
                return self.preorder_print(start.left, traversal) or self.preorder_print(start.right, traversal)
# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

tree.search(4)
tree.print_tree()