class Node(object):

    def __init__(self, value, rChild=None, lChild=None, parent=None):
        self.rChild = rChild
        self.lChild = lChild
        self.parent = parent
        self.value = value
        #self.key = key

    def hasLeftChild(self):
        return self.lChild

    def hasRightChild(self):
        return self.rChild

    def isRoot(self):
        return not self.parent


class Tree(object):

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def add_node(self, value):
        if self.root is None:
            self.root = Node(value)
        elif value < self.root.value:
            self.root.left = self.add_node(self.root.left, Node(value))
        else:
            self.root.right = self.add_node(self.root.right, Node(value))
        return self.root

    def traverse(self, root):
        if root is None:
            return

        self.traverse(self.root.left)
        print(self.)
        self.traverse(self.root.right)


if __name__ == '__main__':
    tree = Tree()
    tree.add_node(5)
    tree.add_node(3)
    tree.add_node(2)
    tree.add_node(1)
