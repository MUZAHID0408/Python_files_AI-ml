
def check_color(graph, color, c, node):
    for adj in graph[node]:
        if color.get(adj) == c:
            return False
    return True

color_list = ['Green', "Blue", "Red", "Yellow", "Orange", "Indigo", "Purple"]

def graph_color_main(graph, color, node_list, index, m):
    if index == len(node_list): #all nodes are colored
        return True
    
    node = node_list[index]
    
    for c in range(0, m):
        if check_color(graph, color, c, node):
            color[node] = c
            if graph_color_main(graph, color, node_list, index + 1, m):
                return True
            color[node] = -1 #restore color if it fails
    
    return False
    

def graph_coloring(graph, m):
    color = {node: -1 for node in graph}
    node_list = list(graph.keys())

    if graph_color_main(graph, color, node_list, 0, m):
        print(f"Graph coloring possible with {m} colors")
        for node in graph:
              print(f" For {node} color is: {color_list[color[node]]}")
        return True   
    else:
        print(f"Coloring not possible with {m} colors")
        return False
    
    
graph={
    1:[3, 5, 6],
    2:[5, 6],
    3:[1, 4, 5],
    4:[3],
    5:[1, 2, 3, 6],
    6:[1, 2, 5]
}

graph_coloring(graph, 3)