class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

    def preorder_traverse(self):
        print(str(self.value) + ' -> ', end='')
        if self.left:
            self.left.preorder_traverse()
        if self.right:
            self.right.preorder_traverse()

    def inorder_traverse(self):
        if self.left:
            self.left.inorder_traverse()
        print(str(self.value) + ' -> ', end='')
        if self.right:
            self.right.inorder_traverse()

    def postorder_traverse(self):
        if self.left:
            self.left.postorder_traverse()
        if self.right:
            self.right.postorder_traverse()
        print(str(self.value) + ' -> ', end='')


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

print("Pre order Traversal: ", end="")
root.preorder_traverse()
print("\nIn order Traversal: ", end="")
root.inorder_traverse()
print("\nPost order Traversal: ", end="")
root.postorder_traverse()