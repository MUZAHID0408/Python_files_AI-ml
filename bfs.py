#user input code in dfs.py file
from collections import deque


def bfs(graph, root):
    visited = set()
    queue = deque([root])
    
    
    while(queue):
        node = queue.popleft()
        if node not in visited:
            print(f'{node} -> ', end="")
            visited.add(node)
            for items in graph[node]:
                if items not in visited:
                    queue.append(items)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph, 'A')


