import time
from Graph import graph
from Graph_db import init_graph

init_graph()
graph.create_adj_matrix()
graph.init_traffic_jams()
start = time.time()
"""for i in range(30):
   a = graph.dijkstra(i)
print(time.time() - start)"""

start = time.time()
for i in range(30):
   a = graph.A_star(i, 1000)
print(time.time() - start)