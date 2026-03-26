from sortedcontainers import SortedList
class Graph:
    def __init__(self, vert_num = None, file = None):
        self.vert_num = 0
        self.edge_num = 0
        self.adj_list = []
        if vert_num:
            self.vert_num = vert_num
            self.generated_adj_list(self.vert_num)
        if file:
            values = file.readlines()
            self.vert_num = int(values[0])
            edges = values[1:]
            self.generated_adj_list(self.vert_num)
            for edge in edges:
                v, w = list(map(int, edge.split()))

                self.add_edge(v, w)

            
    def validate(self, v):
        if v < 0 or v >= self.vert_num:
            print(f"{v} is < 0 or larger than {self.vert_num}")
            raise IndexError
        
    def generated_adj_list(self, vert_num):
        for v in range(vert_num):
            self.adj_list.append(SortedList())
    
    def add_edge(self, v, w):
        self.validate(v)
        self.validate(w)
        
        self.adj_list[v].add(w)
        self.adj_list[w].add(v)
        self.edge_num += 1

    def neighbours(self, v):
        if not self.validate(v):
            return
        return self.adj_list[v]
    
    def degree(self, v):
        if not self.validate(v):
            return
        
        degree = 0
        for neighbour in self.adj_list[v]:
            degree += 1
        return degree
    
    def __str__(self):
        print(f"{self.vert_num} vertices, {self.edge_num} edges")
        for v in range(self.vert_num):
            print(f"{v}: ",end="")
            for neighbour in self.adj_list[v]:
                print(f"{neighbour}",end=" ")
            print()

    