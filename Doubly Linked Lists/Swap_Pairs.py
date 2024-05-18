class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def print_list(self):
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(str(current_node.value))
            current_node = current_node.next
        print(" <-> ".join(output))
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

    def swap_pairs(self):
        if self.length <= 1:
            return False
        temp = self.head
        while temp is not None and temp.next is not None:
            temp.value, temp.next.value = temp.next.value, temp.value
            temp = temp.next.next
            
# # Same logic as above except put temp.next in a variable and it now give nonetype error
    # def swap_pairs(self):
    #     if self.length <= 1:
    #         return False
    #     temp = self.head
    #     after = temp.next
    #     while temp is not None and after is not None:
    #         temp.value, after.value = after.value, temp.value
    #         temp = temp.next.next



my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)

print('my_dll before swap_pairs:')
my_dll.print_list()

my_dll.swap_pairs() 


print('my_dll after swap_pairs:')
my_dll.print_list()