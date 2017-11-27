from heap import *

def dijkstras_withHeap(G,s,t):
    print("Dijkstra running with heap")

    status      = {}
    parent      = {}
    heapFringe  = HeapPQ()
    heapIndex   = {}
    bandwidth   = {}


    bandwidth[s] = float('inf')
    parent[s] = None

    for v in G.get_vertices(): status[v] = 'un_visited'
    status[s] = 'in_tree'

    u = s
    for e in G.get_connected_edges(s):
        #print (e)
        v = e[1]
        bandwidth[v] = e[2]
        status[v] = 'fringe'
        parent[v] = u
        heapIndex[v] = heapFringe.add(bandwidth[v],v)

    while (status[t] != 'in_tree'):
        #u = max(fringe, key=fringe.get)
        #max_bw = fringe[u]
        #fringe.__delitem__(u)

        max_element = heapFringe.remove_largest()
        print(max_element)
        max_wt = max_element[0]
        v      = max_element[1]
        u      = parent[v]
        print(heapIndex)
        #heapIndex.__delitem__(u)

        bandwidth[u] = max_wt
        #print("Vertex: ", u,"Weight:", max_bw)
        status[u] = 'in_tree'
        #Standard Dijkstras's core implementation : Source = notes + online
        #print(G.get_connected_edges(u))
        for e in G.get_connected_edges(u):
            #print(e)
            vertex = e[1]

            if  status[vertex] == 'un_visited':
                status[vertex] = 'fringe'
                parent[vertex] = u
                bandwidth[vertex] = min(bandwidth[u], e[2])
                heapIndex[vertex] = heapFringe.add(bandwidth[vertex], vertex)

            elif status[vertex] == 'fringe' and bandwidth[vertex] < min(bandwidth[u], e[2]):
                parent[vertex] = u
                bandwidth[vertex] = min(bandwidth[u], e[2])
                heapFringe.update(locator[vertex], bw[vertex], vertex)

    if status[t] == 'in_tree':

        max_bw = bandwidth[t]
        while(parent[t] != None):
            print(t, "<-- ", end="")
            t = parent[t]
        print(t)

        print("Max_bandwidth:",max_bw )