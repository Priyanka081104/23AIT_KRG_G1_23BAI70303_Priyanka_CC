def makeConnected(n, connections):
    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        pa, pb = find(a), find(b)
        if pa != pb:
            parent[pa] = pb
            return True
        return False

    extra = 0
    for u, v in connections:
        if not union(u, v):
            extra += 1

    components = len(set(find(i) for i in range(n)))
    needed = components - 1

    return needed if extra >= needed else -1
