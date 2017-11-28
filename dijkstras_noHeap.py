def dijkstras_noHeap(G,s,t):
    print("Dijkstra running without heap")
    status      = {}
    parent      = {}
    fringe      = {}
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
        fringe[v] = bandwidth[v]



    while (status[t] != 'in_tree'):
        u = max(fringe, key=fringe.get)
        #print (u)
        max_bw = fringe[u]
        fringe.__delitem__(u)
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
                fringe[vertex] = bandwidth[vertex]

            elif status[vertex] == 'fringe' and bandwidth[vertex] < min(bandwidth[u], e[2]):
                parent[vertex] = u
                bandwidth[vertex] = min(bandwidth[u], e[2])
                fringe[vertex] = bandwidth[vertex]


    if status[t] == 'in_tree':

        count = 0;
        max_bw = bandwidth[t]
        while(parent[t] != None and t != s):
            print(t, "<-- ", end="")
            t = parent[t]
            count +=1

        print(t)
        #print("Last: ",  t)

        print("Max_bandwidth:",max_bw )
