from heap import *
from graph import Graph
from queue import *

root = {}
rank = {}

def make_set(vertex):
    root[vertex] = vertex
    rank[vertex] = 0

def union(vertex1, vertex2):
    root1 = find(vertex1)
    root2 = find(vertex2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            root[root2] = root1
        elif rank[root1] < rank[root2]:
            root[root1] = root2
        else:
            root[root2] = root1
            rank[root1] += 1

def find(vertex):
    if root[vertex] != vertex:
        root[vertex] = find(root[vertex])
    return root[vertex]

def kruskals(G,s,t):
    print("Kruskal is walking thru the graph slowly...")
    Pqueue  = HeapPQ()
    for v in G.get_vertices(): make_set(v)
    for e in G.get_edges()   :
        #print(e)
        Pqueue.add(e[2],e)

    #Pqueue.show()

    mst     = Graph()
    start_v   = s
    end_v     = t

    while(len(Pqueue.elementList)>0):
        max_element = Pqueue.remove_largest()
        #print("Removing:",max_element[0])
        #Pqueue.show()

        max_wt = max_element[0]
        u      = max_element[1][0]
        v      = max_element[1][1]

        u_root = find(u)
        v_root = find(v)

        if(u_root != v_root):
            if u not in mst.get_vertices():
                mst.add_vertex(u)
            if v not in mst.get_vertices():
                mst.add_vertex(v)
            mst.add_edge(u,v,max_wt)
            union(u,v)

    #print ("MST is",mst._edge)
    max_bw = BFS(mst,start_v,end_v)
    print("Max Bandwidth:", max_bw)

def BFS(mst,s,t):
    start = s

    visited = []
    visited.append(s)

    queue = set()
    queue.add(s)

    parent = {}
    parent[s] = 0

    while queue:
        vertex = queue.pop()
        for neighbour in mst.get_adjacent_vertices(vertex):
            if neighbour not in visited:
                visited.append(neighbour)
                queue.add(neighbour)
                parent[neighbour] = vertex

            if neighbour == t:
                t_parent = vertex
                print(t, "<-- ", end="")
                max_bw = mst.get_edge(vertex,t)[2]

                while parent[vertex] != 0:
                    print(vertex,"<-- ", end="")
                    bw = mst.get_edge(vertex, parent[vertex])[2]
                    if(bw<max_bw):
                        max_bw = bw
                    vertex = parent[vertex]

                print(vertex)
                return max_bw
