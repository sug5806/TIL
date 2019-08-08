import copy


class ShortestPath:
    def __init__(self, A, path):
        self.A = A
        self.path = path

    def print_path(self, src, dst):
        print(src, end="  ")
        self.__print_sp(src, dst)
        print(dst, end= "  ")

    def __print_sp(self, i, j):
        # base case
        if self.path[i][j] is None:
            return

        k = self.path[i][j]
        self.__print_sp(i, k)
        print(k, end="  ")
        self.__print_sp(k, j)


class Graph:
    INF = 99999

    def __init__(self, v_num):
        self.adjacency_matrix = [[Graph.INF for _ in range(v_num) for _ in range(v_num)]]
        for i in range(v_num):
            self.adjacency_matrix[i][i] = 0
        self.vertex_num = v_num

    def insert_edge(self, u, v, w):
        # 방향 그래프, 가중치 그래프
        self.adjacency_matrix[u][v] = w

    def floyd_warshall(self):
        # A^-1
        A = copy.deepcopy(self.adjacency_matrix)
        path = [[None for _ in range(self.vertex_num)] for _ in range(self.vertex_num)]

        for k in range(self.vertex_num):
            for i in range(self.vertex_num):
                for j in range(self.vertex_num):
                    # A^(k-1)[i][j]     A^(k-1)[i][k] + A^(k-1)[k][j]
                    if A[i][j] > A[i][k] + A[k][j]:
                        A[i][j] = A[i][k] + A[k][j]
                        path[i][j] = k

        return 1


if __name__ == "__main__":
    g = Graph(6)
    g.insert_edge(0, 1, 5)
    g.insert_edge(0, 2, 7)
    g.insert_edge(0, 5, 9)
    g.insert_edge(1, 3, 4)
    g.insert_edge(1, 5, 2)
    g.insert_edge(2, 0, 8)
    g.insert_edge(2, 4, 6)
    g.insert_edge(3, 0, 6)
    g.insert_edge(3, 4, 2)
    g.insert_edge(3, 5, 3)
    g.insert_edge(4, 2, 3)
    g.insert_edge(4, 5, 10)
    g.insert_edge(5, 1, 7)
    g.insert_edge(5, 2, 4)

    source = 2
    dest = 3

    sp = g.floyd_warshall()

    print("A mat")
    for i in range(g.vertex_num):
        for j in range(g.vertex_num):
            print("{}".format(sp.A[i][j]).rjust(4), end="")
        print()
    print()

    print("path mat")
    for i in range(g.vertex_num):
        for j in range(g.vertex_num):
            if sp.path[i][j] is None:
                print("{} ".format("N").rjust(4), end="")
            else:
                print("{} ".format(sp.path[i][j]).rjust(4), end="")
        print()
    print()
    #
    print("path from {} to {}".format(source, dest))
    sp.print_shortest_path(source, dest)
    print()
