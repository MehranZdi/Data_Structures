class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def preorder_traversal(self):
        print(str(self.data) + ' --> ', end='')
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(str(self.data) + ' --> ',                     end='')
        if self.right:
            self.right.inorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(str(self.data) + ' --> ', end='')


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)

    print('Preorder Traversal:')
    root.preorder_traversal()
    print(f'\nInorder Traversal:')
    root.inorder_traversal()
    print(f'\npostorder Traversal:')
    root.postorder_traversal()
