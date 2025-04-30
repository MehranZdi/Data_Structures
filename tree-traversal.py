class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.value = item

def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.value) + ' -> ', end='')
        inorder(root.right)


def preorder(root):
    if root:
        print(str(root.value) + ' -> ', end='')
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.value) + ' -> ', end='')


root = Node(1)
left_child = Node(12)
right_child = Node(9)
root.left = left_child
root.right = right_child
left_child.left = Node(5)
left_child.right = Node(6)

inorder(root)
