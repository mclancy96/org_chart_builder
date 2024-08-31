import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from mapping import mapping

# Load spreadsheet
df = pd.read_json('all_active_titles.json')

# Create graph
G = nx.from_pandas_edgelist(df,
                            source='managed_by_title_id',
                            target='id',
                            create_using=nx.MultiGraph)
H = nx.relabel_nodes(G, mapping)

# Create layout and display
pos = nx.nx_agraph.pygraphviz_layout(H, prog="twopi", root=0)
nx.draw(H, pos, with_labels=True, font_size=6, node_size=1)
plt.show()
