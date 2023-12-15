from RMP import dict_gn

def DFS(graph, start, goal):
    stack = []
    visited_node = set()
    stack.append(start)

    path=[]

    while len(stack)!=0:
        current = stack.pop()
        
        if current not in visited_node:
            visited_node.add(current)
            path.append(current)

            if current == goal:
                print("Path :  ", " -> ".join(path))
                return

            for eachneighbour in graph[current]:
                stack.append(eachneighbour)

DFS(dict_gn, "Arad", "Bucharest")