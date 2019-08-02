from MST.disjoint_set import DisjointSet


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

    def MST_kruskal(self):
        mst = Graph(self.vertex_num)
        ds = DisjointSet(self.vertex_num)
        self.edge_list.sort(key=lambda e: e.w)

        mst_edge_num = 0
        edge_idx = 0
        while mst_edge_num < self.vertex_num - 1:
            edge = self.edge_list[edge_idx]
            # 사이클이 있는지 체크
            # 사이클이 없다면 현재 edge를 선택한다
            if ds.collapsing_find(edge.u) != \
                    ds.collapsing_find(edge.v):
                # 에지를 선택
                mst.insert_edge(edge.u, edge.v, edge.w)
                ds.weighted_union(ds.collapsing_find(edge.u),
                                  ds.collapsing_find(edge.v))
                mst_edge_num += 1
            edge_idx += 1

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

    mst = g.MST_kruskal()

    mst.print_edges()
