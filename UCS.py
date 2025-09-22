import heapq

def uniform_cost_search(G, start, finish):
    dilewati = set()
    queue = [(0, start, [start])] 
    
    while queue:
        cost, node, path = heapq.heappop(queue)

        if node == finish:
            return path, cost

        if node in dilewati:
            continue
        dilewati.add(node)

        for anakan, data in G.get(node,[]):
            if anakan not in dilewati:
                heapq.heappush(queue, (cost + data, anakan, path + [anakan]))

    return None, float("inf")
