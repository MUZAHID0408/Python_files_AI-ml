#how to take input in dfs graph
#using dictionary

def dfs (graph, root):
    stack = [root]
    visited = set()
    
    while stack:
        node = stack.pop()
        if node not in visited:
            print(f"{node} ->", end="")
            visited.add(node)
            for items in reversed(graph[node]):
                if items not in visited:
                    stack.append(items)
                
    
    


graph2 = {
    'A':['B', 'C'],
    'B':['A', 'C', 'D'],
    'C':['A', 'B', 'D','E'],
    'D':['B', 'C','E'],
    'E':['C','D']
}
def take_userinput():
    graph = {}
    num = int(input("Enter the number of vertices: "))
    for i in range(1, num+1):
        key =input("Enter the key: ")
        value = input("Enter the values space seperated: ").split()
        graph[key] = value

    dfs(graph, 'C')


dfs(graph2,'C')    
    




