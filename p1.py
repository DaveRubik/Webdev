# Implmentation of BFS and DFS

import collections

def BFS(graph, root):
    visited, queue = set()
    collections.deque([root])
    visited.add(root)
    while queue:
        vertex = queue.popleft()
        print(str(vertex)+" ", end="")
        for nb in graph[vertex]:
            if nb not in visited:
                visited.add(nb)
                queue.append(nb)
    

def DFS(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end="")
    for next in graph[start]:
        print("->", end="")
        DFS(graph, next, visited)
    return visited