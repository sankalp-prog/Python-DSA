class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        v_list = []
        for vertex in self.adj_list:
            v_list.append(vertex)
        v_list.sort()
        for v in v_list:
            print(v, ':', self.adj_list[v])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = set()
            return True 
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
                self.adj_list[v1].add(v2)
                return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for v in self.adj_list:
                # Don't have to do the following check i I use discard() instead of remove()
                # if vertex in self.adj_list[v]:
                     self.adj_list[v].discard(vertex)
            del self.adj_list[vertex]
            return True
        return False

    def remove_edge(self, v1, v2):
        '''Takes input (v1, v2) and then removes the edge v1 -> v2'''
        if v1 in self.adj_list and v2 in self.adj_list:
            # if v2 in self.adj_list[v1]:
                self.adj_list[v1].discard(v2)
                return True
        return False

my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A','B')
# checking if duplicate edges can be added
my_graph.add_edge('A','B')
my_graph.add_edge('A','C')
my_graph.add_edge('A','D')
my_graph.add_edge('B','D')
my_graph.add_edge('B','A')
my_graph.add_edge('C','D')

# print('Graph before remove_edge():')
# my_graph.print_graph()


# my_graph.remove_edge('A', 'D')


# print('\nGraph after remove_edge():')
# my_graph.print_graph()

print('Graph before remove_vertex():')
my_graph.print_graph()


my_graph.remove_vertex('D')

print('\nGraph after remove_vertex():')
my_graph.print_graph()