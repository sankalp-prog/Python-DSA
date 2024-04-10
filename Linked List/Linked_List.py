class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        if self.length == 0:
            print(None)
        # while temp is not None:
        # OR 
        while temp: # None = False, any other value return True
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        # When the list has no nodes 
        if self.length == 0:
            return None
        # General case
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        # When the list popped it's only node
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        # if list has no node
        if self.length == 0:
            return None
        # General case
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        # if list had only one node
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index > self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    # I would rather name it update_value
    def set_value(self, index, value):
        temp = self.get(index)
        if temp is None:
            return False
        temp.value = value
        return True
# # my solution before looking at course solution - 
# 
#     def insert(self, index, value):
#         if index < 0 or index > self.length:
#             return False 
#         new_node = Node(value)
#         new_node.next = self.get(index)
#         if index == 0:
#             self.head = new_node
#         else:
#             temp = self.get(index - 1)
#             temp.next = new_node
#         if self.length == 0:
#             self.tail = new_node
#         self.length += 1
#         return True


    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False 
        if index == 0:
            return self.prepend(value)
        if self.length == 0:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
        
    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        self.tail, self.head = self.head, self.tail
        pre = None
        temp = self.tail
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = pre
            pre = temp
            temp = after
        return True


link = LinkedList(4)
link.append(5)
link.append(6)
link.append(7)
link.append(8)
link.reverse()
link.print_list()