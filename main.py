import networkx as nx
import pandas as pd
from pyvis.network import Network
from UCS import uniform_cost_search

df = pd.read_csv("graph.csv")

G = nx.Graph()
for _, row in df.iterrows():
    G.add_edge(row["asal"],row["tujuan"],weight=row["weight"])

mulai = "Cilegon"
tujuan = "Banyuwangi"

path, cost = uniform_cost_search(G, mulai, tujuan)

print("Rute UCS:", "→".join(path) if path else "not found")
print("Total jarak:", cost,"km")

net = Network(height="700px", width="100%", bgcolor="#222222", font_color="white")

# kalau path None, set jadi list kosong biar tidak error
if path is None:
    path = []

# Buat set edge dari path
path_edges = set(zip(path, path[1:]))

for u, v, data in G.edges(data=True):
    edge_color = "red" if (u, v) in path_edges or (v, u) in path_edges else "blue"
    node_color_u = "orange" if u in path else "lightblue"
    node_color_v = "orange" if v in path else "lightblue"

    net.add_node(u, label=u, color=node_color_u)
    net.add_node(v, label=v, color=node_color_v)
    net.add_edge(u, v, value=data["weight"], title=f"{data['weight']} km", color=edge_color)

html_file = "graph_jawa_UCS.html"
net.save_graph(html_file)

with open(html_file,"r",encoding="utf-8") as f:
    html_content=f.read()

information = f""" 
<div style="padding:15px; background:#333; color:white; font-family:Arial; margin-top:20px;">
    <h2>Hasil Uniform Search:</h2>
    <p><b>Rute:</b> {"→".join(path)}</p>
    <p><b>Total Jarak ditemput:</b> {cost} km </p>
</div>
"""

html_content = html_content.replace("</body>", information + "</body>")

with open(html_file,"w",encoding="utf-8") as f:
    f.write(html_content)

print(f"Graph berhasil dibuat di {html_file}")