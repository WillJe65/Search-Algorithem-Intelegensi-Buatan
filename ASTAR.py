import heapq

#Algoritma start search
def a_star_search(G, start, goal, heuristic):

    # f(n) = g(n) + h(n)
    g_cost = 0
    h_cost = heuristic[start]
    f_cost = g_cost + h_cost
    

    queue = [(f_cost, g_cost, start, [start])] 
    visited = set()

    #perulangan logic untuk mencari rute terbaik
    while queue:
        _f_cost, g_cost, node, path = heapq.heappop(queue)

        #jika ketemu goal
        if node == goal:
            return path, g_cost

        #jika sudah dikunjungi
        if node in visited:
            continue
        visited.add(node)

        #untuk mengecek apakah node lain dari note
        for neighbor, weight in G[node]:   
            if neighbor not in visited:
                new_g_cost = g_cost + weight
                new_h_cost = heuristic[neighbor]  
                new_f_cost = new_g_cost + new_h_cost

                heapq.heappush(queue, (new_f_cost, new_g_cost, neighbor, path + [neighbor]))
    #mengembalikan nilai
    return None, float("inf")
