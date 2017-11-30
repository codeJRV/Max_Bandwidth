import graph
import random
import time

def generate_graph( n_vertex,max_wt, degree ):

    if degree >= 500:
        print("Generating a relatively dense graph, this will take some time....")
    else:
        print("Sparse graph generation, should happen quickly...")


    start_time = time.time()
    end_time   = 0
    g = graph.Graph()
    for index in range(1, n_vertex + 1):
        g.add_vertex(index)


    st_list = []
    while(len(st_list)<5):

        s = 0
        t = 0
        while (s == t):
            s = random.randint(1, n_vertex - 1)  # randomly select a vertex s and t
            t = random.randint(1, n_vertex - 1)

            print("start:",s,"end",t)
            start = s

        #create a path from s to t
        for u in g.get_vertices():
            if u == t or u == s:
                continue
            else:
                weight = random.randint(1, max_wt)
                if(g.graph_degree(start)<degree):
                    if(start != u):
                        g.add_edge(start, u, weight)

                start = u

        wt = random.randint(1, max_wt)
        if (g.graph_degree(start) < degree): g.add_edge(start, t, wt)

        if (s,t) not in st_list:
            st_list.append((s,t))


    #now we need to ensure each vertex is connected to atleast degree number of vertexes
    #vertex_list

    vertex_list = g.get_vertices()

    while(len(vertex_list)>2):  # atleast two valid vertices
        u = vertex_list.pop()
        u_degree = g.graph_degree(u)
        for p in range(u_degree,degree):
            if(len(vertex_list)>0):
                v = random.choice(vertex_list)

                if(g.get_edge(u,v)==-1 and g.graph_degree(v)<degree):
                    wt = random.randint(1, max_wt)
                    if(u != v):
                        g.add_edge(u,v,wt)

                if (g.graph_degree(v) == degree):
                    vertex_list.remove(v)

    end_time = time.time()

    print ("Graph of ", n_vertex, " vertices with ", end="")
    #print(g._edge)

    print("Average degree:", float(sum(g.graph_degree(v) for v in g.get_vertices()))/float(n_vertex),"is generated")


    #print(g.n_edges())
    #print(g.n_vertices())

    return g,st_list,(end_time-start_time)
