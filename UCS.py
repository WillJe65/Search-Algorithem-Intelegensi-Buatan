import heapq

#algoritma uniform cost search
def uniform_cost_search(G, start, finish):
    visited = set()
    queue = [(0, start, [start])] 
    
    #perulangan untuk mencari rute ke goal didalam graph 
    while queue:
        cost, node, path = heapq.heappop(queue)

        #jika sampai goal
        if node == finish:
            return path, cost

        #jika sudah dikunjungi
        if node in visited:
            continue
        visited.add(node)

        #mengecek apakah node tetangga dari node sekarang belum dikunjungi atau belum dengan mempertimbangkan costnya
        for anakan, data in G.get(node,[]):
            if anakan not in visited:
                heapq.heappush(queue, (cost + data, anakan, path + [anakan]))

    return None, float("inf")
