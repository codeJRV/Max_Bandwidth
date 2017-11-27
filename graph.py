class Graph:
    def __init__(self):
        self._edge = {}  #create a dictionary of vertices as keys and edges as values

    def get_vertices(self):
        v = set(self._edge.keys())
        #print("Returning vertices",v)
        return v

    def get_edges(self):
        e = set()
        for map in self._edge.values():(e.update(map.values()))
        #print("Returning edges",e)
        return e

    def n_edges(self):
        num_edges = (sum(len(self._edge[v]) for v in self._edge.keys()))
        print("Number of edges", num_edges)
        return num_edges

    def n_vertices(self):
        num_vetices = len(self._edge)
        print("Number of vertices", num_vetices)
        return num_vetices

    def add_vertex(self, index):
        self._edge[index] = {}    #create an entry for the vertex


    def add_edge(self, u, v, weight):
        #print("adding edge",u,v,weight)
        self._edge[u][v] = (u, v, weight)
        self._edge[v][u] = (v, u, weight)

    def get_adjacent_vertices(self, v):                         #done
        return list(self._edge[v].keys())

    def get_connected_edges(self, v):
        connected_edges = self._edge[v].values()
        #print("Incident_edges", connected_edges)
        return list(connected_edges)

    def get_edge(self, u, v):
        if(self._edge[u].get(v)):
            e = self._edge[u].get(v)
        else:
            e = -1
        return e

    def get_other_end(self,e,v):
        p,q,w = e
        if v == p:
            return q
        if v == q:
            return p

    def graph_degree(self, v ):
        if(v<len(self._edge)):
            degree = len(self._edge[v])
        else:
            degree = 0
        return degree

    def grap_plot(self):
        print(self)
        return self