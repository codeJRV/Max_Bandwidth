class Graph:
    __slots__ = '_edge'

    def __init__(self):
        self._edge = {}
        #create a dictionary of vertices as keys and edges as values

    def get_vertices(self):
        #print("SelfKeys", self._edge.keys())
        v = list(self._edge.keys())
        #print("Returning vertices",v)
        return v

    def get_edges(self):
        #print(self._edge)
        l = []
        for v in list(self._edge.items()):
            for e in list(v[1].items()):
                l.append((v[0],e[0],e[1]))
        return l


    def add_vertex(self, index):
        self._edge[index] = {}    #create an entry for the vertex


    def add_edge(self, u, v, weight):
        #print("adding edge",u,v,weight)
        self._edge[u][v] = (weight)
        self._edge[v][u] = (weight)

    def get_adjacent_vertices(self, v):                         #done
        return list(self._edge[v].keys())

    def get_connected_edges(self, v):
        connected_edges =  self._edge[v].items()
        #print("Incident_edges", connected_edges)
        return list(connected_edges)

    def get_edge(self, u, v):
        #print("self_edge" ,u, v, self._edge)
        if(self._edge[u].get(v)):
            #print("self edge" ,self._edge[u][v],v)
            return self._edge[u][v]
        else:
            return -1


    def graph_degree(self, v ):
        if(v<len(self._edge)):
            degree = len(self._edge[v])
        else:
            degree = 0
        return degree

    def grap_plot(self):
        print(self._edge)
        return self