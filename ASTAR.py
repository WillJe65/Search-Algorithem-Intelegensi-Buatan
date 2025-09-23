import heapq

def a_star_search(graph, heuristic, start, goal):
    visited = set()
    pq = [(heuristic.get(start, 0), 0, start, [start])]

    while pq:
        f_cost, cost_so_far, node, path = heapq.heappop(pq)

        if node == goal:
            return path, cost_so_far

        if node in visited:
            continue
        visited.add(node)

        for neighbor, dist in graph.get(node, []):
            if neighbor not in visited:
                new_cost = cost_so_far + dist
                priority = new_cost + heuristic.get(neighbor, 0)
                heapq.heappush(pq, (priority, new_cost, neighbor, path + [neighbor]))

    return None, float('inf')