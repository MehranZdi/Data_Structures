class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:                        #base case
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(12)
    root.right = Node(9)
    root.left.left = Node(5)
    root.left.right = Node(6)
    print(f'The result of preorder traversal is:')
    preorder(root)
    print(f'The result of inorder traversal is:')
    inorder(root)
    print(f'The result of inorder traversal is:')
    postorder(root)