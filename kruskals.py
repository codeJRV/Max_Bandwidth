from graph import Graph
from heap import *
import time

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

def kruskals(G,st_list,to_see):
    print("Kruskal is walking thru the graph slowly...")
    start_time = time.time()
    end_time   = 0
    Pqueue  = HeapPQ()
    for v in G.get_vertices(): make_set(v)
    for e in G.get_edges()   :
        #print(e)
        Pqueue.add(e[2],e)

    #Pqueue.show()

    mst     = Graph()

    while(len(Pqueue)>0):
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


    end_time = time.time()
    #print ("MST is",mst._edge)

    for s,t in st_list:
        part_time = time.time()
        max_bw = BFS(mst,s,t,to_see)
        part_time_end = time.time()
        print("start", s, "end", t, end="")
        print(" Max Bandwidth:", max_bw, end="")
        print(" Runtime(taking MST generation+ BFS(s-t)): ", format((end_time-start_time) + (part_time -part_time_end)) , "seconds" )

    end_time = time.time()



    return (end_time-start_time)

def BFS(mst,s,t,to_see):
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
                if(to_see == '0'): print(t, "<-- ", end="")
                #print("Edge" ,mst.get_edge(vertex,t))
                max_bw = mst.get_edge(vertex,t)

                while parent[vertex] != 0:
                    if (to_see == '0'): print(vertex,"<-- ", end="")
                    bw = mst.get_edge(vertex, parent[vertex])
                    if(bw<max_bw):
                        max_bw = bw
                    vertex = parent[vertex]

                if (to_see == '0'): print(vertex)
                return max_bw
