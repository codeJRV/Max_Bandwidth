from generate_random_graphs import *
from heap import *
import graph
import time
from kruskals import *
from dijkstras_noHeap import *
from dijkstras_withHeap import *
import time

n = 0
g_time  = []
k_time  = []
d_time  = []
dh_time = []

while (n < 3):


    start_time = time.time()
    G,s,t = generate_graph(5000,50,1000)
    end_time = time.time()
    print("Graph Generation takes time", format(end_time -start_time), "seconds")

    g_time.append((end_time-start_time))

    start_time = time.time()
    kruskals(G, s, t)
    end_time = time.time()

    k_time.append((end_time-start_time))

    print("kruskals algorithm takes time", format(end_time -start_time), "seconds")

    start_time = time.time()
    dijkstras_noHeap(G,s,t)
    end_time = time.time()
    print("Dijkstras algorithm takes time", format(end_time -start_time), "seconds")
    d_time.append((end_time-start_time))

    start_time = time.time()
    dijkstras_withHeap(G,s,t)
    end_time = time.time()
    print("Dijkstras algorithm with heap takes time", format(end_time -start_time), "seconds")
    dh_time.append((end_time-start_time))

    n += 1

print( "Average g time: ", float(sum(g_time))/float(n))
print( "Average k time: ", float(sum(k_time))/float(n))
print( "Average d time: ", float(sum(d_time))/float(n))
print( "Average dh time: ", float(sum(dh_time))/float(n))