from lstack import LStack

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def empty(self):
        if not self.head:
            return True
        return False

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    
    def traverse(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next

class Position:
    def __init__(self, row, col, dir):
        self.row = row
        self.col = col
        self.dir = dir

class MazeSolver:
    direction=((-1, 0), (-1, 1), 
    (0, 1), (1, 1), (1, 0), 
    (1, -1), (0, -1), (-1, -1))


# 처음에는 자기의 위치와 조사할 위치를 전달함
# 스택은 position을 저장함
# mark -> 방문 했는지 안했는지 확인용
# maze -> 벽이 있는지 없는지
# 갈곳이 없을경우 스택에서 pop을 해서 왔던 곳으로 돌아감

    def __init__(self, maze):
        self.maze = maze
        # leng = len(maze)
        self.EXIT_ROW = len(maze)    # 출구 행
        self.EXIT_COL = len(maze[0]) # 출구 열

        # to do : 맨 위 아래 옆에 1로된 벽 넣기
        for row in maze:
            row.insert(0, 1)
            row.append(1)
    
        added_row = [1 for _ in range(self.EXIT_COL+2)]
        maze.insert(0, added_row)
        maze.append(added_row)

        self.path = LinkedList()
       
    
    def get_path(self):
        stack=LStack()
        mark=[]
        # mark를 0으로 채워진 실제 미로크기의 리스트로 만들어라
        for _ in range(self.EXIT_ROW+2):
            mark.append([0 for _ in range(self.EXIT_COL+2)])

        row = None; col = None; dir= None;
        next_row = None; next_col = None;
        found=False

        # 미로의 시작점(1, 1)

        mark[1][1] = 1
        # 첫 시작 위치를 스택에 push
        stack.push(Position(1, 1, 2))

        # 스택이 비어있다면 경로가 없다.
        while not stack.empty() and not found:
            temp = stack.pop()
            row = temp.row
            col = temp.col
            dir = temp.dir
            # dir을 다 돌기전에 찾으면 나감
            while dir < 8 and not found: 
                next_row = row + self.direction[dir][0]
                next_col = col + self.direction[dir][1]
                if self.maze[next_row][next_col] != 1 and mark[next_row][next_col] == 0:
                    stack.push(Position(row, col, dir))
                    row = next_row
                    col = next_col
                    mark[row][col] = 1
                    dir = 0
                elif row == self.EXIT_ROW and col == self.EXIT_COL:
                    stack.push(Position(row, col, dir))
                    found = True

                else:
                    dir += 1
                    
                

        if found:
            while not stack.empty():
                self.path.add(stack.pop())
        else:
            print('There is no path in this maze!')

    def print_path(self):
            g = self.path.traverse()
            for node in g:
                print("({}, {})".format(node.data.row, node.data.col))

    def show_maze(self):
        print('   ', end='')
        for i in range(self.EXIT_ROW+2):
            print(' ' + str(i) + ' ', end='')
        print()
        for i in range(self.EXIT_ROW+2):
            print(' ' + str(i) + ' ', end='')
            for j in range(self.EXIT_COL+2):
                if self.maze[i][j] == 0:
                    print(' O ', end='')
                else:
                    print(' # ', end='')
            print()
        print()

    def show_path(self):
        path_set = set()
        g=self.path.traverse()
        for node in g:
            path_set.add((node.data.row, node.data.col))
        
        print('   ', end='')
        for i in range(self.EXIT_ROW+2):
            print(' ' + str(i) + ' ', end='')
        print()

        for i in range(self.EXIT_ROW+2):
            print(' ' + str(i) + ' ', end='')

            for j in range(self.EXIT_COL+2):
                if (i, j) in path_set:
                    print(' P ', end='')
                elif self.maze[i][j] == 0:
                    print(' O ', end='')
                else:
                    print(' # ', end='')
            print()
        print()




if __name__ == "__main__":
    maze = [
		[0, 1, 1, 0, 0],
		[1, 0, 0, 1, 1],
		[0, 1, 1, 0, 1],
		[0, 1, 0, 1, 1],
		[1, 1, 0, 0, 0],
    ]

    maze_solver = MazeSolver(maze)
    maze_solver.show_maze()
    maze_solver.get_path()
    maze_solver.print_path()
    maze_solver.show_path()