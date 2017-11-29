from generate_random_graphs import *
from kruskals import *
from dijkstras_noHeap import *
from dijkstras_withHeap import *
import time

n = 0
g_time  = []
k_time  = []
d_time  = []
dh_time = []

while (n < 1):



    G,s,t, runtime = generate_graph(500,999,100)
    print("Graph Generation takes time", format(runtime), "seconds")
    g_time.append((runtime))


    runtime = kruskals(G, s, t)
    k_time.append((runtime))
    print("kruskals algorithm takes time", format(runtime), "seconds")

    runtime = dijkstras_noHeap(G,s,t)
    print("Dijkstras algorithm takes time", format(runtime), "seconds")
    d_time.append((runtime))

    runtime = dijkstras_withHeap(G,s,t)
    print("Dijkstras algorithm with heap takes time", format(runtime), "seconds")
    dh_time.append((runtime))

    n += 1

print( "Average g time: ", float(sum(g_time))/float(n))
print( "Average k time: ", float(sum(k_time))/float(n))
print( "Average d time: ", float(sum(d_time))/float(n))
print( "Average dh time: ", float(sum(dh_time))/float(n))