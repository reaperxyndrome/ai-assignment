# maze graph is represented with (1,1) coordinate as top-left
# and 5,5 as bottom-right
maze_graph = {
    (1, 1): [(1, 2)],
    (1, 2): [(1, 1), (1, 3)],
    (1, 3): [(1, 2), (1, 4)],
    (1, 4): [(1, 3), (1, 5), (2, 4)],
    (1, 5): [(1, 4)],
    (2, 1): [(2, 2), (3, 1)],
    (2, 2): [(2, 1), (2, 3)],
    (2, 3): [(2, 2), (2, 4)],
    (2, 4): [(1, 4), (2, 3), (2, 5), (3, 4)],
    (2, 5): [(2, 4), (3, 5)],
    (3, 1): [(2, 1), (4, 1)],
    (3, 2): [(4, 2)],
    (3, 3): [(4, 3)],
    (3, 4): [(2, 4)],
    (3, 5): [(2, 5), (4, 5)],
    (4, 1): [(3, 1), (4, 2)],
    (4, 2): [(3, 2), (4, 1)],
    (4, 3): [(3, 3), (4, 2), (5, 3)],
    (4, 4): [(5, 4)],
    (4, 5): [(3, 5), (5, 5)],
    (5, 1): [(5, 2)],
    (5, 2): [(5, 1), (5, 3)],
    (5, 3): [(4, 3), (5, 2), (5, 4)],
    (5, 4): [(4, 4), (5, 3), (5, 5)],
    (5, 5): [(4, 5), (5, 4)]
}

def path_from_trace(trace):
    path = []
    if goal in trace:
        parent = trace[goal]
        path.append(goal)
        while parent:
          path.append(parent)
          parent = trace[parent]
    return path

def DFS(graph, start, target):
    print("depth first search of the maze graph:\n")
    visited = set()
    Q = []
    Q.append( (None, start) )
    trace = {}

    while Q:
        (parent, current) = Q.pop()
        trace[current] = parent

        # keep track of visited nodes
        visited.add(current)
        print("visited: ", current)

        # check if the goal is reached
        if current == target:
           print("reached target: ", target)
           break

        for neighbor in graph[current]:
          not_visited = neighbor not in visited
          not_in_queue = (current, neighbor) not in Q
          if not_visited and not_in_queue :
            Q.append((current, neighbor) )
            print("added neighbour: ", neighbor)

        print("Q: ", Q)
    return trace

start = (1, 1)
goal = (3, 2)

trace_DFS = DFS(maze_graph, start, goal)
path_DFS = path_from_trace(trace_DFS)
print(f"The path from start to goal is {path_DFS[::-1]} ")