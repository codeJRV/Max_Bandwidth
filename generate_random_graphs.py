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

    s = 0
    t = 0

    while (s == t):
        s = random.randint(1, n_vertex - 1)  # randomly select a vertex s and t
        t = random.randint(1, n_vertex - 1)

    print("start:",s,"end",t)
    start = s
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


    #now we need to ensure each vertex is connected to atleast degree number of vertexes
    #vertex_list
    #print(g._edge)
    vertex_list = list(v for v in g.get_vertices())

    for v in vertex_list:
        if(g.graph_degree(v)==degree):
            vertex_list.remove(v)

    while(len(vertex_list)>1):  # atleast two valid vertices
        u = vertex_list.pop()
        v = random.choice(vertex_list)
        added = False
        if(g.get_edge(u,v)==-1 and g.graph_degree(u)<degree and g.graph_degree(v)<degree):
            wt = random.randint(1, max_wt)
            if(u != v):
                g.add_edge(u,v,wt)
                added = True

        if(g.graph_degree(u)<degree and added == True):
            vertex_list.append(u)

        if (g.graph_degree(v) < degree and added == True):
            vertex_list.append(v)

    end_time = time.time()

    print ("Graph of ", n_vertex, " vertices with ", end="")
    #print(g._edge)

    print("Average degree:", float(sum(g.graph_degree(v) for v in g.get_vertices()))/float(n_vertex),"is generated")


    #print(g.n_edges())
    #print(g.n_vertices())

    return g,s,t,(end_time-start_time)
