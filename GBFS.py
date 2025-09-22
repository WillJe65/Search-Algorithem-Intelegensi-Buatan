import heapq

def greedy_bfs(graph, heuristic, start, goal):
    visited = set()
    pq = [(heuristic.get(start, 0), start, [start], 0)]  # (h(n), node, path, cost_so_far)

    while pq:
        h, node, path, cost_so_far = heapq.heappop(pq)
        if node == goal:
            return path, cost_so_far
        if node in visited:
            continue
        visited.add(node)

        for neighbor, dist in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic.get(neighbor, 0), neighbor, path + [neighbor], cost_so_far + dist))

    return None, float('inf')
