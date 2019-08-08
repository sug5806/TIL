class ShortestPath:
    def __init__(self, src, dist, p):
        self.source = src
        self.distance = dist
        self.pre = p

    # 재귀 함수
    def print_path(self, dst):
        # 1. base case
        if self.source == dst:
            print(dst, end="  ")
            return

        # 2.
        # 언제 호출 할 것인가?
        if self.pre[dst] is not None:
            self.print_path(self.pre[dst])
            return

        else:
            print("There is no path")
            return


class Graph:
    INF = 99999

    def __init__(self, v_num):
        self.adjacency_matrix = [[None for _ in range(v_num)] for _ in range(v_num)]
        self.vertex_num = v_num

    def insert_edge(self, u, v, w):
        self.adjacency_matrix[u][v] = w

    def find_min(self, distance, s):
        _min = 9999999
        min_v = None

        for v in range(self.vertex_num):
            if distance[v] < _min and v not in s:
                _min = distance[v]
                min_v = v

        return min_v

    def dijkstra(self, src):
        s = set()
        distance = [Graph.INF for _ in range(self.vertex_num)]
        pre = [None for _ in range(self.vertex_num)]
        distance[src] = 0

        while len(s) < self.vertex_num:
            v = self.find_min(distance, s)
            s.add(v)

            # adj[v]
            for u in range(self.vertex_num):
                w = self.adjacency_matrix[v][u]
                # w != None --> adj[v] 안에 u가 포함
                # u not in s --> u는 아직 s안에 미포함
                # RELAXATION : distance[u] < distance[v]
                if w is not None and u not in s and distance[u] > distance[v] + w:
                    distance[u] = distance[v] + w
                    pre[u] = v

        return ShortestPath(src, distance, pre)


if __name__ == "__main__":
    g = Graph(4)
    g.insert_edge(0, 1, 10)
    g.insert_edge(0, 2, 3)
    g.insert_edge(1, 3, 5)
    g.insert_edge(2, 1, 5)
    g.insert_edge(2, 3, 8)
    g.insert_edge(3, 1, 4)
    g.insert_edge(3, 2, 12)

    source = 0
    sp = g.dijkstra(source)
    for i in range(g.vertex_num):
        print(f"distance[{i}] : {sp.distance[i]}, p[{i}] : {sp.pre[i]}")

    print(f'{sp.source} to {}')
    sp.print_path(3)