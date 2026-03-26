from queue import Queue
class BFS:
    def __init__(self):
        return
    
    def traverse(self, graph):
        visited = set()
        path = []
        queue = Queue()

        v = self.starting_vertex(graph)
        queue.put(v)
        visited.add(v)

        while not queue.empty():
            current = queue.get()
            path.append(current)

            for neighbour in graph.neighbours(current):
                if neighbour not in visited:
                    queue.put(neighbour)
                    visited.add(neighbour)
        
        return path


    def starting_vertex(self, graph):
        graph.__str__()
        user_input = input("Enter Vertex: ")
        return int(user_input)

    def print_path(self, path):
        print("==================================================")
        print("Bredth First Search Traversal Map")
        print("==================================================")
        for vertex in path:
            print(f"{vertex}",end=" ")
        print()
        print("==================================================")