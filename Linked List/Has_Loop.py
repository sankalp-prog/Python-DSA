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

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

# # My solution that worked without looking at course solution
# # Noob mistake returning False in the while loop as the while loop will end anyways, should have put it outside

#     def has_loop(self):
#         fast_pointer = self.head
#         slow_pointer = self.head
#         while fast_pointer and fast_pointer.next:
#             fast_pointer = fast_pointer.next.next
#             slow_pointer = slow_pointer.next
#             if fast_pointer is slow_pointer:
#                 return True
#             if fast_pointer is None:
#                 return False

# Course Solution -
    def has_loop(self):
        fast_pointer = self.head
        slow_pointer = self.head
        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
            if fast_pointer is slow_pointer:
                return True
        return False
    
    
    
    
my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head
print(my_linked_list_1.has_loop() ) # Returns True




my_linked_list_2 = LinkedList(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
print(my_linked_list_2.has_loop() ) # Returns False



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    
"""
