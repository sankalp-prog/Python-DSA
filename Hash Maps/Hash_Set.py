class HashSet:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, value):
        my_hash = 0
        for char in value:
            my_hash = hash(char) % len(self.data_map)
        # print(f"hash value: {my_hash}")
        return my_hash

    def print_values(self):
        answer_list = []
        for values in self.data_map:
            if values:
                for value in values:
                    answer_list.append(value)
        print(answer_list)

    def add(self, value):
        index = self.__hash(value)
        if self.contains(value):
            return
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append(value)

    def contains(self, value):
        index = self.__hash(value)
        if self.data_map[index] is None:
            return False
        if value in self.data_map[index]:
            return True 
        return False
        

my_set = HashSet()
my_set.add("H")
my_set.add("H")
my_set.add("I")
my_set.add("G")
my_set.print_values()
print(my_set.contains("G"))
