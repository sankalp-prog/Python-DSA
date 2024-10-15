# post-order: visits left subtree, then right subtree and then current node
# pre-order: visits current node, then left subtree and then right subtree
# inorder: visits left subtree, then current Node and then right subtree

class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.right = right
        self.left = left

def inorder(tree: Node, func):
    if tree is None:
        return

    inorder(tree.left, func)
    func(tree.val)
    inorder(tree.right, func)

def preorder(tree: Node, func):
    if tree is None:
        return

    func(tree.val)
    preorder(tree.left, func)
    preorder(tree.right, func)

def postorder(tree: Node, func):
    if tree is None:
        return

    postorder(tree.left, func)
    postorder(tree.right, func)
    func(tree.val)


a = Node(1, None, None)
c = Node(3, None, None)
e = Node(5, None, None)
g = Node(7, None, None)
b = Node(2, a, c)
f = Node(6, e, g)
root = Node(4, b, f)

my_list = []
inorder(root, lambda a: my_list.append(a))
print(my_list)

my_list = []
preorder(root, lambda a: my_list.append(a))
print(my_list)

my_list = []
postorder(root, lambda a: my_list.append(a))
print(my_list)
