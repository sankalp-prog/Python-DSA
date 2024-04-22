class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
# # MY FIRST SOLUTION
    # def append(self, value):
    #     new_node = Node(value)
    #     if self.length == 0:
    #         self.head = new_node
    #         self.tail = new_node
    #         self.length += 1
    #         return True
    #     temp = self.head
    #     while temp.next:
    #         temp = temp.next 
    #     temp.next = new_node
    #     new_node.prev = temp
    #     self.tail = new_node
    #     self.length += 1
    #     return True

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        new_node.prev = self.tail 
        self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None 
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.previous = None
        self.length -= 1
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
        
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - index - 1):
                temp = temp.prev
        return temp 

    # My solution -
    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return False
        else:
            temp = self.get(index)
            temp.value = value
            return True
        
    # # Course Solution - 
    # def set_value(self, index, value):
    #     temp = self.get(index)
    #     if temp:
    #         temp.value = value
    #         return True
    #     return False

    # My Solution - 
    def insert(self, index, value):
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        temp = self.get(index)
        new_node = Node(value)
        if temp:
            temp.prev.next = new_node
            new_node.next = temp
            new_node.prev = temp.prev
            temp.prev = new_node
            self.length += 1
            return True
        return False
    
    # # Course Solution -
    # def insert(self, index, value):
    #     if index < 0 or index > self.length:
    #         return False
    #     if index == 0:
    #         return self.prepend(value)
    #     if index == self.length:
    #         return self.append(value)
 
    #     new_node = Node(value)
    #     before = self.get(index - 1)
    #     after = before.next
 
    #     new_node.prev = before
    #     new_node.next = after
    #     before.next = new_node
    #     after.prev = new_node
        
    #     self.length += 1   
    #     return True 

    # My solution and course solution is almost same -
    def remove(self, index):
        temp = self.get(index)
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        if temp:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            temp.prev = None
            temp.next = None
            self.length -= 1
            return temp
        return None


