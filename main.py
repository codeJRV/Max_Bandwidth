from generate_random_graphs import *
from heap import *
import graph
import time
from kruskals import *
from dijkstras_noHeap import *
from dijkstras_withHeap import *



#G,s,t = generate_graph(500,19,9)
G = Graph()
G.add_vertex(1)
G.add_vertex(2)
G.add_vertex(3)
G.add_vertex(4)
G.add_vertex(5)

G.add_edge(1,2,9)
G.add_edge(1,3,7)
G.add_edge(2,3,2)
G.add_edge(2,4,3)
G.add_edge(3,5,5)
G.add_edge(4,5,6)

s = 1
t = 4


start_time = time.time()
kruskals(G, s, t)
dijkstras_noHeap(G,s,t)
#dijkstras_withHeap(G,s,t)
