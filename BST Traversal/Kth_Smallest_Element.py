class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
                
    # had to look at solution
    def kth_smallest(self, k):
        stack = []
        node = self.root
        
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.value
            
            node = node.right
            
        return None



bst = BinarySearchTree()

bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print(bst.kth_smallest(1))  # Expected output: 2
print(bst.kth_smallest(3))  # Expected output: 4
print(bst.kth_smallest(6))  # Expected output: 7


"""
    EXPECTED OUTPUT:
    ----------------
    2
    4
    7

 """