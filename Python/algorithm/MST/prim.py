import math


# Graph representaion : adjacency list

class GNode:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
        self.link = None


class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


# 그래프는 객체와 객체 사이의 관계
# 새로운 노드(정점)을 추가하는 경우가 거의 없다!!
class Graph:
    def __init__(self, vnum):
        self.adjacency_list = [None for _ in range(vnum)]
        self.edge_list = []
        self.vertex_num = vnum

    def __add_node(self, v, unode):
        pass

    def insert_edge(self, u, v, w):
        unode = GNode(u, w)
        vnode = GNode(v, w)
        self.__add_node(u, vnode)
        self.__add_node(v, unode)
        self.edge_list.append(Edge(u, v, w))

    def get_min_v(self, w):
        _min = math.inf
        min_idx = None
        for i in range(len(w)):
            if _min > w[i]:
                _min = w[i]
                min_idx = i
        return min_idx

    def MST_prim(self):
        mst = Graph(self.vertex_num)
        TV = set()
        w = [math.inf for _ in range(self.vertex_num)]
        _from = [None for _ in range(self.vertex_num)]
        w[0] = 0

        while len(TV) < self.vertex_num:
            v = self.get_min_v(w)
            # TV = TV U {v}
            # TE = TE U {(v, from[v])}
            # each u in adj[v]
            TV.add(v)
            if _from[v] is not None:
                mst.insert_edge(v, _from[v], w[v])
            # 핵심 알짜
            w[v] = math.inf
            # adj[v]
            u = self.adjacency_list[v]
            while u:
                if u.vertex not in TV and u.weight < w[u.vertex]:
                    w[u.vertex] = u.weight
                    _from[u.vertex] = v
                u = u.link
        return mst
    # 테스트를 위한 코드
    def print_edges(self):
        for edge in self.edge_list:
            print(f'({edge.u}, {edge.v}) : {edge.w}')


if __name__ == "__main__":
    g = Graph(6)

    g.insert_edge(0, 1, 10)
    g.insert_edge(0, 2, 2)
    g.insert_edge(0, 3, 8)
    g.insert_edge(1, 2, 5)
    g.insert_edge(1, 4, 12)
    g.insert_edge(2, 3, 7)
    g.insert_edge(2, 4, 17)
    g.insert_edge(3, 4, 4)
    g.insert_edge(3, 5, 14)

    mst = g.MST_prim()

    mst.print_edges()
