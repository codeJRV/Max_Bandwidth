from heap import *
import time

def dijkstras_withHeap(G,s,t):
    print("Dijkstra running with heap")
    start_time = time.time()
    end_time   = 0
    status      = {}
    parent      = {}
    fringe      = DijkstrasHeap(None,None)
    bandwidth   = {}
    indexer     = {}


    bandwidth[s] = float('inf')
    parent[s] = None

    for v in G.get_vertices():
        status[v] = 'un_visited'

    status[s] = 'in_tree'

    u = s
    for e in G.get_connected_edges(s):
        #print (e)
        v = e[1]
        #print (v)
        bandwidth[v] = e[2]
        status[v] = 'fringe'
        parent[v] = u

        indexer[v] = fringe.add(bandwidth[v],v)
        # print("Added vertex:", v, "to fringe, index", indexer[v]._index)
        # print (indexer[v]._index," ", end="")
        # print(indexer[v]._key, " ", end="")
        # print(indexer[v]._value)


    #print (indexer)
    #fringe.show()

    #print("till here ok")

    while (status[t] != 'in_tree'):

        max_element = fringe.remove_largest()
        #print("Removing:",max_element[1], "of weight",max_element[0] )
        #Pqueue.show()

        max_bw = max_element[0]
        u      = max_element[1]
        uIndex = indexer[u]._index
        indexer.pop(u)


        for v in indexer:
            if(indexer[v]._index > uIndex):
                indexer[v]._index -= 1
            # print(indexer[v]._index, " ", end="")
            # print(indexer[v]._key, " ", end="")
            # print(indexer[v]._value)

        bandwidth[u] = max_bw
        #print("Vertex: ", u,"Weight:", max_bw)
        status[u] = 'in_tree'
        #Standard Dijkstras's core implementation : Source = notes + online
        #print(G.get_connected_edges(u))
        for e in G.get_connected_edges(u):
            #print("Edge:", e)
            vertex = e[1]
            #print("Vertex: ", vertex)
            #print(status[vertex])

            if  status[vertex] == 'un_visited':
                status[vertex] = 'fringe'
                parent[vertex] = u
                bandwidth[vertex] = min(bandwidth[u], e[2])
                #fringe[vertex] = bandwidth[vertex]
                indexer[vertex] = fringe.add(bandwidth[vertex], vertex)
                #print("Added vertex:", vertex,"to fringe, index", indexer[vertex]._index)

            elif status[vertex] == 'fringe' and (bandwidth[vertex] < min(bandwidth[u], e[2])):
                parent[vertex] = u
                bandwidth[vertex] = min(bandwidth[u], e[2])
                #fringe[vertex] = bandwidth[vertex]
                #print("Updating vertex:",vertex,"to new index",indexer[vertex]._index)

                fringe.update(indexer[vertex],bandwidth[vertex],vertex)


    if status[t] == 'in_tree':

        max_bw = bandwidth[t]
        end_time = time.time()
        while(parent[t] != None and t != s):
            print(t, "<-- ", end="")
            t = parent[t]
        print(t)

        print("Max_bandwidth:",max_bw )

    return (end_time-start_time)