class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX
            return True
        return False


def has_bottleneck_spanning_tree(G, b):
    edges = []
    for u, v, w in G:
        if w <= b:
            edges.append((u, v, w))

    edges.sort(key=lambda x: x[2])
    uf = UnionFind(len(G))
    components = len(G)

    for u, v, w in edges:
        if uf.union(u, v):
            components -= 1
        if components == 1:
            return True

    return False


# 示例用法
G = [(0, 1, 2), (1, 2, 3), (2, 3, 4), (3, 0, 5)]
b = 4
print(has_bottleneck_spanning_tree(G, b))  # 输出: True


def bottleneck_spanning_tree(G):
    edges = sorted(G, key=lambda x: x[2])
    uf = UnionFind(len(G))
    max_weight = 0
    mst_edges = []

    for u, v, w in edges:
        if uf.union(u, v):
            mst_edges.append((u, v, w))
            max_weight = max(max_weight, w)
            if len(mst_edges) == len(G) - 1:
                break

    return mst_edges, max_weight


# 示例用法
G = [(0, 1, 2), (1, 2, 3), (2, 3, 4), (3, 0, 5)]
mst_edges, max_weight = bottleneck_spanning_tree(G)
print("MST Edges:", mst_edges)
print("Max Weight:", max_weight)