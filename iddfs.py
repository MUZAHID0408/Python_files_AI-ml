def iddfs_found(graph, target, depth_limit, root):
    stack = [(root, 0)]
    visited = set()
    
    while (stack):
        node, depth = stack.pop()
        if node not in visited:
            print(f"{node} -> ", end="")
            visited.add(node)
        
            if node  == target:
                return True
            
            if depth < depth_limit:
                for items in reversed(graph.get(node, [])):
                    stack.append((items, depth + 1))            
    return False        
                
    
    

def iddfs(graph, target, max_depth, root):
    for depth in range(max_depth+1):
       print(f"Searching for depth {depth}: ")
       if iddfs_found(graph, target, depth, root):
           print()
           print(f"Found the result at depth {depth}")
           return True
       print() 
    print("Max depth reached result not found...")
    return False



graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
iddfs(graph, 'F', 2, 'A')

