from UCS import uniform_cost_search
from GBFS import greedy_bfs
from ASTAR import a_star_search
import csv

def load_graph(file_path):
    graph = {}
    with open(file_path,'r')as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            asal = row['asal'].strip()
            tujuan = row['tujuan'].strip()
            jarak = int(row['weight'])

            if asal not in graph:
                graph[asal] = []
            graph[asal].append((tujuan,jarak))

            #graph yang dianggap dua arah
            if tujuan not in graph:
                graph[tujuan] = []
            graph[tujuan].append((asal,jarak))
        return graph
    
def load_heuristik(file_path):
    h = {}
    with open(file_path,'r') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            kota = row['asal'].strip()
            heuristik = int(row['heuristik'])
            h[kota] = heuristik
        
    return h

if __name__ == "__main__":
    graph_file = "graph.csv"
    heuristik_file = "heuristik.csv"
    astar_file = "heuristik.csv"

    graph = load_graph(graph_file)
    heuristik = load_heuristik(heuristik_file)

    start_kota = "Cilegon"
    goal_kota = "Banyuwangi"

    #UCS
    ucs_path, ucs_cost = uniform_cost_search(graph,start_kota,goal_kota)
    print("UNIFORM COST SEARCH (UCS)")
    print("Rute = ","->".join(ucs_path))
    print("Jarak total = ", ucs_cost," km \n")

    #GBFS
    gbfs_path, gbfs_cost = greedy_bfs(graph, heuristik,start_kota, goal_kota)
    print("GREEDY BACK TRACKING IDK (GBFS)")
    print("Rute = ","->".join(gbfs_path))
    print("Jarak total = ", gbfs_cost," km ")

<<<<<<< HEAD
    #A*
    astar_path,astar_cost = a_star_search(graph,start_kota,goal_kota,heuristik)
    print("A Star Search (A*)")
    print("Rute = ","->".join(astar_path))
    print("Jarak total = ", astar_cost," km ")
=======
    #A*
    astar_path, astar_cost = a_star_search(graph, heuristik,start_kota, goal_kota)
    print("\nA STAR (A*)")
    print("Rute = ","->".join(astar_path))
    print("Jarak total = ", astar_cost," km ")


>>>>>>> 0f53254dd38d559bc48a81e07a7a3b1930eea876