def floyd_warshall(graph):
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for u in range(n):
        for v, weight in graph[u]:
            dist[u][v] = weight

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def find_best_road(G, E_prime):
    n = len(G)
    dist = floyd_warshall(G)
    best_reduction = 0
    best_pair = None

    for u, v, l_prime in E_prime:
        new_dist = [[dist[i][j] for j in range(n)] for i in range(n)]

        for i in range(n):
            for j in range(n):
                new_dist[i][j] = min(new_dist[i][j], dist[i][u] + l_prime + dist[v][j])
                new_dist[i][j] = min(new_dist[i][j], dist[i][v] + l_prime + dist[u][j])

        reduction = max(dist[s][t] - new_dist[s][t] for s in range(n) for t in range(n))

        if reduction > best_reduction:
            best_reduction = reduction
            best_pair = (u, v)

    return best_pair, best_reduction


# 示例用法
G = [
    [(1, 5), (2, 3)],
    [(2, 2), (3, 6)],
    [(3, 7)],
    []
]

E_prime = [
    (0, 3, 4),
    (1, 3, 3)
]

best_pair, best_reduction = find_best_road(G, E_prime)
print("Best pair:", best_pair)
print("Best reduction:", best_reduction)