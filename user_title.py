import pandas as pd
import networkx as nx
# import matplotlib.pyplot as plt
from select_ids_for_tree import select_ids_for_tree
from mapping_newlines import mapping

# Load spreadsheet
df = pd.read_json('all_active_titles.json')
# Filter from a root node
df = df[df["id"].isin(select_ids_for_tree(2615, 'all_active_titles.json'))]

# Create graph
G = nx.from_pandas_edgelist(df,
                            source='managed_by_title_id',
                            target='id',
                            create_using=nx.MultiGraph)
H = nx.relabel_nodes(G, mapping)


# Create layout and display
pos = nx.nx_agraph.pygraphviz_layout(H, prog="twopi", root=0)
nx.nx_agraph.write_dot(H, 'dot_graph.dot')
# nx.draw(H, pos, with_labels=True, font_size=6, node_size=1)
# plt.show()
