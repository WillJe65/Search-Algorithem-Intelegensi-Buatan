import heapq

#main fungsi greedy
def greedy_bfs(graph, heuristic, start, goal):

    visited = set()
    pq = [(heuristic.get(start, 0), start, [start], 0)]  # (h(n), node, jalur, costnya)

    #perulangan untuk melakukan tracking pada node
    while pq:
        h, node, path, cost_so_far = heapq.heappop(pq)

        #jika ketemu goal
        if node == goal:
            return path, cost_so_far
        
        #jika sudah dikunjungi
        if node in visited:
            continue
        visited.add(node)

        #mengecek apakah node tetangga dari node sekarang belum dikunjungi atau belum dengan mempertimbangkan costnya
        for neighbor, dist in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic.get(neighbor, 0), neighbor, path + [neighbor], cost_so_far + dist))

    return None, float('inf')
