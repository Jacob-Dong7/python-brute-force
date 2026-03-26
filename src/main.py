import os
from graph import Graph
from dfs import DFS
from bfs import BFS
def main():
    while True:
        print("\n==================================================")
        print("Brute Force Searching Algorithms")
        print("==================================================")
        print("[1] Depth First Search")
        print("[2] Bredth First Search")
        print("[-1] Quit")
        print("==================================================\n")
        user_input = input("Select option: ")
        if user_input == "1":
            file = get_file()
            try:
                with open(file) as f:
                    graph = Graph(file=f)
            except FileNotFoundError:
                print("Error: file not found")
                continue
            algorithm = DFS()
            path = algorithm.traverse(graph)
            algorithm.print_path(path)
        elif user_input == "2":
            file = get_file()
            try:
                with open(file) as f:
                    graph = Graph(file=f)
            except FileNotFoundError:
                print("Error: file not found")
                continue
            algorithm = BFS()
            path = algorithm.traverse(graph)
            algorithm.print_path(path)
        
        elif user_input == "-1":
            quit()


def get_file():
    graph = file()
    return graph

def file():
    print("==================================================")
    user_input = input("Enter graph name: ")
    print("==================================================")
    return os.path.join("graphs", user_input)

if __name__ == "__main__":
    main()
