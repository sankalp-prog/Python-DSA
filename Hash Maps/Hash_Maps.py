class HashMaps:
    def __init__(self, size = 7):
        self.data_map = [None] * size
      
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash  

    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    # course solution:
    # def get_item(self, key):
    #     index = self.__hash(key)
    #     if self.data_map[index] is not None:
    #         for i in range(len(self.data_map[index])):
    #             if self.data_map[index][i][0] == key:
    #                 return self.data_map[index][i][1]
    #     return None
    
    # My Solution:
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index]:
            for pair in self.data_map[index]:
                if pair[0] == key:
                    return pair[1]
        return None

    # Course Solution:
    # def keys(self):
    #     all_keys = []
    #     for i in range(len(self.data_map)):
    #         if self.data_map[i] is not None:
    #             for j in range(len(self.data_map[i])):
    #                 all_keys.append(self.data_map[i][j][0])
    #     return all_keys

# My Solution:
    def keys(self):
        all_keys = []
        for pairs in self.data_map:
            if pairs:
                for pair in pairs:
                    all_keys.append(pair[0])
        return all_keys





