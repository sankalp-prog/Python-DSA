# Did wihout using numpy
class Graph:
    def __init__(self, n):
        self.num_of_vertex = n
        self.adj_matrix = [[0]*n for _ in range(n)]

    def print_graph(self):
        for i in range(self.num_of_vertex):
            print(f'{i} ->', end='    ')
            for j in range(self.num_of_vertex):
                print(self.adj_matrix[i][j], end="   ")
            print("\n")

    def add_edge(self, v1, v2):
        '''Taking (v1, v2) as input and creating the edge v1 -> v2'''
        if 0 < v1 < 5 and 0 < v2 < 5:
            self.adj_matrix[v1][v2] = True
            return True
        return False
        
    def remove_edge(self, v1, v2):
        if 0 < v1 < 5 and 0 < v2 < 5:
            self.adj_matrix[v1][v2] = False

my_graph = Graph(5)
my_graph.add_edge(1,2)
# checking if duplicate edges can be added
my_graph.add_edge(1,2)
my_graph.add_edge(1,3)
my_graph.add_edge(1,4)
my_graph.add_edge(2,4)
my_graph.add_edge(2,1)
my_graph.add_edge(3,4)

print('Graph before remove_edge():')
my_graph.print_graph()


my_graph.remove_edge(1, 4)


print('\nGraph after remove_edge():')
my_graph.print_graph()