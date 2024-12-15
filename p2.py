# Implement Water Jug Algoritm

from collections import deque

def waterJugProblem(cap_a, cap_b, target):
    queue = deque([((0,0), [])])
    visited = set()
    while queue:
        (a, b), path = queue.popleft()
        if a == target or b == target:
            return path +[(a, b)]
        nextStates = [
            (cap_a, b),
            (a, cap_b),
            (0, b),
            (a, 0),
            (min(a+b, cap_a), max(0, a+b-cap_a)),
            (max(0, a+b-cap_b), min(a+b, cap_b))
        ]
        
        for next in nextStates:
            if next not in visited:
                visited.add(next)
                queue.append((next, path+[(a,b)]))
    return None

cap_a = 5
cap_b = 8
tgt = 4
path = waterJugProblem(cap_a, cap_b, tgt)
if path is None:
    print("No possible solutions")
else:
    for state in path:
        print(state)