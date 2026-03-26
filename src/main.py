import os
from graph import Graph
def main():
    file = get_file()
    try:
        with open(file) as f:
            graph = Graph(file=f)
    except FileNotFoundError:
        print("Error: File not found")
    
    graph.__str__()
    return

def get_file():
    user_input = input("Enter file name: ")
    return os.path.join("graphs", user_input)


if __name__ == "__main__":
    main()