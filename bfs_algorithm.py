#Eren Ali Aslangiray
#213911362
import pickle



G = [[0, 1, 0, 1, 0, 0 ], [0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 1, 0]]

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

def find_shortest_path (G):
    Graph = {}
    for i in range (0, len(G)):
        for j in range (0, len(G[i])):
            if G[i][j] == 0:
                a = i,j
                b = str(a)
                c = set ([])
                if i == 0:
                    if j == 0:
                        if G[i + 1][j] == 0:
                            a1 = i + 1, j
                            b1 = str(a1)
                            c.add(b1)
                        if G[i][j + 1] == 0:
                            a2 = i, j + 1
                            b2 = str(a2)
                            c.add(b2)
                    else:
                        try:
                            if G[i + 1][j] == 0:
                                a3 = i + 1, j
                                b3 = str(a3)
                                c.add(b3)
                        except:
                            1
                        try:
                            if G[i][j + 1] == 0:
                                a4 = i, j + 1
                                b4 = str(a4)
                                c.add(b4)
                        except:
                            1
                        try:
                            if G[i][j -1] == 0:
                                a5 = i, j - 1
                                b5 = str(a5)
                                c.add(b5)
                        except:
                            1
                elif j == 0:
                    try:
                        if G[i + 1][j] == 0:
                            a6 = i + 1, j
                            b6 = str(a6)
                            c.add(b6)
                    except:
                        1
                    try:
                        if G[i][j + 1] == 0:
                            a7 = i, j + 1
                            b7 = str(a7)
                            c.add(b7)
                    except:
                        1
                    try:
                        if G[i-1][j] == 0:
                            a8 = i-1, j
                            b8 = str(a8)
                            c.add(b8)
                    except:
                        1
                else:
                    try:
                        if G[i + 1][j] == 0:
                            a9 = i + 1, j
                            b9 = str(a9)
                            c.add(b9)
                    except:
                        1
                    try:
                        if G[i][j + 1] == 0:
                            a10 = i, j + 1
                            b10 = str(a10)
                            c.add(b10)
                    except:
                        1
                    try:
                        if G[i-1][j] == 0:
                            a11 = i-1, j
                            b11 = str(a11)
                            c.add(b11)
                    except:
                        1
                    try:
                        if G[i][j-1] == 0:
                            a12 = i, j-1
                            b12 = str(a12)
                            c.add(b12)
                    except:
                        1

                Graph[b] = c
    list(bfs_paths(Graph, '(0, 0)', '(3, 5)'))
    print shortest_path(Graph, '(0, 0)', '(3, 5)')

find_shortest_path(G)






