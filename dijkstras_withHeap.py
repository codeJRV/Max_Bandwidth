from heap import *

def dijkstras_withHeap(G,s,t):
    print("Dijkstra running with heap")
    status      = {}
    parent      = {}
    fringe      = DijkstrasHeap(None,None)
    bandwidth   = {}
    indexer     = {}


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
        indexer[v] = fringe.add(bandwidth[v],v)

    #print (indexer)
    #fringe.show()

    #print("till here ok")

    while (status[t] != 'in_tree'):

        max_element = fringe.remove_largest()
        #print("Removing:",max_element[0])
        #Pqueue.show()

        max_bw = max_element[0]
        u      = max_element[1]

        indexer.__delitem__(u)
        bandwidth[u] = max_bw
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
                #fringe[vertex] = bandwidth[vertex]
                indexer[vertex] = fringe.add(bandwidth[vertex], vertex)

            elif status[vertex] == 'fringe' and bandwidth[vertex] < min(bandwidth[u], e[2]):
                parent[vertex] = u
                bandwidth[vertex] = min(bandwidth[u], e[2])
                #fringe[vertex] = bandwidth[vertex]
                fringe.update(indexer[vertex],bandwidth[vertex],vertex)

    if status[t] == 'in_tree':

        max_bw = bandwidth[t]
        while(parent[t] != None):
            print(t, "<-- ", end="")
            t = parent[t]
        print(t)

        print("Max_bandwidth:",max_bw )
