import networkx as nx
import matplotlib.pyplot as plt

graph = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9),
         (2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
G = nx.DiGraph()
for idx, edge in enumerate(graph):
    G.add_edge(*edge, weight=idx)
    # G.add_edge(*edge)
    # G[edge[0]][edge[1]]['weight'] = idx

pos=nx.shell_layout(G)
# pos=nx.spring_layout(G,iterations=100)
# nx.draw(G, pos)
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos)
plt.show()
