from queue import Queue


class Stack:
    def __init__(self):
        self.container = list()

    def push(self, data):
        self.container.append(data)

    def pop(self):
        self.container.pop()

    def peek(self):
        return self.container[-1]

    def empty(self):
        if not self.container:
            return True
        else:
            return False


class Gnode:
    def __init__(self, v):
        # self.__vertex = v
        # self.__link = None
        self.vertex = v
        self.link = None

        # @property
        # def vertex(self):
        #     return self.__vertex
        #
        # @vertex.setter
        # def vertex(self, v):
        #     self.__vertex = v
        #
        # @property
        # def link(self):
        #     return self.__link
        #
        # @link.setter
        # def link(self, Node):
        #     self.__link = Node


class Graph:
    def __init__(self, v_num):
        self.adjacency_list = [None for _ in range(v_num)]
        # 방문했는지 체크하기 위함
        self.visited = [False for _ in range(len(self.adjacency_list))]

    def __add_node(self, v, u_node):
        cur = self.adjacency_list[v]
        if cur is None:
            self.adjacency_list[v] = u_node
            return

        while cur.link:
            cur = cur.link
        cur.link = u_node

    def insert_edge(self, u, v):
        u_node = Gnode(u)
        v_node = Gnode(v)
        self.__add_node(v, u_node)
        self.__add_node(u, v_node)

    def bfs(self, start):
        q = Queue()
        visited = [False for _ in range(len(self.adjacency_list))]

        q.put(start)
        visited[start] = True

        # 방문
        print(start, end=" ")

        while not q.empty():
            # dequeue
            v = q.get()

            # adj[v]
            u_Node = self.adjacency_list[v]
            while u_Node:
                if not visited[u_Node.vertex]:
                    q.put(u_Node.vertex)
                    visited[u_Node.vertex] = True
                    # visited
                    print(u_Node.vertex, end=" ")
                u_Node = u_Node.link

    def __dfs__recursion(self, start):
        # base case
        # if self.visited[start]:
        #     return

        self.visited[start] = True
        # 방문
        print(start, end="  ")

        # adj[v]
        u_Node = self.adjacency_list[start]
        while u_Node:
            if not self.visited[u_Node.vertex]:
                # base case2
                self.__dfs__recursion(u_Node.vertex)
            u_Node = u_Node.link

    def dfs(self, start):
        # 방문 리스트 초기화
        for i in range(len(self.adjacency_list)):
            self.visited[i] = False

        self.__dfs__recursion(start)

    def dfs_iter(self, v):
        s = Stack()
        for i in range(len(self.visited)):
            self.visited[i] = False

        s.push(v)
        self.visited[v] = True
        print(v, end="  ")

        while not s.empty():
            is_visited = False
            v = s.peek()
            u_Node = self.adjacency_list[v]
            while u_Node:
                if not self.visited[u_Node.vertex]:
                    self.visited[u_Node.vertex] = True
                    print(u_Node.vertex, end="  ")
                    s.push(u_Node.vertex)
                    is_visited = True
                    break
                u_Node = u_Node.link
            if not is_visited:
                s.pop()


if __name__ == "__main__":
    g = Graph(6)
    g.insert_edge(0, 3)
    g.insert_edge(0, 1)
    g.insert_edge(2, 4)
    g.insert_edge(2, 5)
    g.insert_edge(3, 4)

    # 3, 0, 4, 1, 2, 5
    # g.bfs(3)

    # 3, 0, 1, 4, 2, 5
    g.dfs(3)
    print()
    g.dfs_iter(3)

