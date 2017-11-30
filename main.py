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

print("Enter 1 to generate the sparse graph in project and run over 10 ( 5 pairs) graphs, each with 5 s-t pairs")
print("Enter 2 to generate the sparse graph in project and run over 10 ( 5 pairs) graphs, each with 5 s-t pairs")
print("Enter 3 to generate custom graph each with 5 s-t pairs")

instr = input('<<')

if (instr == '1'):
    n_vertices = 5000
    conn       = 8
    max_wt     = 999
    testcases  = 10
    to_see     = 1

elif (instr == '2'):
    n_vertices = 5000
    conn       = 1000
    max_wt     = 999
    testcases  = 10
    to_see     = 1

else:

    print('Enter number of vertices: ')
    n_vertices = input('n_vertices: ')

    print('Enter avg number of connected vertices of any vertex (should be < n_vertices) : ')
    conn = input('vertices: ')

    if(int(conn) > int(n_vertices)):
        raise Exception('Cannot generate this graph')


    print('Enter max weight: ')
    max_wt = input('max_wt: ')


    print('Enter number of graphs ( each testcase has 5 start and end points')
    testcases = input('graphs:')

    print('Enter 0 if you want to see the generated paths')
    to_see  = input('To see(0) or not to see(any other number): ')


while (n < int(testcases)):

    G,st_list, runtime = generate_graph(int(n_vertices),int(max_wt),int(conn))
    print("Graph Generation takes time", format(runtime), "seconds ")
    g_time.append((runtime))

    runtime = dijkstras_noHeap(G, st_list,to_see)
    print("Dijkstras algorithm takes average time", format(runtime/5), "seconds per s-t path")
    d_time.append((runtime))
    #
    runtime = dijkstras_withHeap(G, st_list, to_see)
    print("Dijkstras algorithm with heap takes average time", format(runtime/5), "seconds per s-t path")
    dh_time.append((runtime))

#
#
#
    runtime = kruskals(G, st_list,to_see)
    k_time.append((runtime))
    print("kruskals algorithm takes average time", format(runtime/5), "seconds per s-t path")
#

#
    n += 1
#
print( "Average Graph Generation time over all test cases       : ", float(sum(g_time))/float(n))
print( "Average Kruskals MST time over all test cases           : ", float(sum(k_time))/float(n*5))
print( "Average Mod-Dijkstras time over all test cases          : ", float(sum(d_time))/float(n*5))
print( "Average Mod-Dijkstras with Heap time over all test cases: ", float(sum(dh_time))/float(n*5))