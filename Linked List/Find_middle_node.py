class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    # only have to create the function, rest all was already given
# First solution[didn't read the requirements where it said to use 2 pointer method]
    def find_middle_node(self):
        if self.head is None:
            return None
        length = 0
        temp = self.head
        while temp.next:
            temp = temp.next
            length += 1
        if length == 1:
            return self.head 
        middle = self.head
        for _ in range(length//2):
            middle = middle.next
        return middle
        # solution doesn't work for even lists, by using floor division, value returned is not the latter but earlier than the middle

    # # Solution after looking at the requirements, had trouble with the while loop condition, rest all was identical
    # def find_middle_node(self):
    #     slow_pointer = self.head
    #     fast_pointer = self.head
    #     while fast_pointer is not None and fast_pointer.next is not None:
    #         fast_pointer = fast_pointer.next.next
    #         slow_pointer = slow_pointer.next
    #     return slow_pointer


            
'''Requirements: 
1. The method should use a two-pointer approach, where one pointer (slow) moves one node at a time 
    and the other pointer (fast) moves two nodes at a time.

2. When the fast pointer reaches the end of the list or has no next node, 
    the slow pointer should be at the middle node of the list.

3. The method should return the middle node or the first node of the second half of the list
     if the list has an even number of nodes.

4. The method should only traverse the linked list once.  In other words, you can only use one loop.
'''


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
# my_linked_list.append(5)

print( my_linked_list.find_middle_node().value )



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""