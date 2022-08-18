import sys


class DequeWoojin():

    def __init__(self):
        self._list = []

    def __len__(self):
        return len(self._list)

    def push_right(self, value):
        self._list.append(value)

    def push_left(self, value):
        self._list.insert(0, value)

    def pop_right(self):
        return self._list.pop()

    def pop_left(self):
        return self._list.pop(0)

    def peek_right(self):
        return self._list[-1]

    def peek_left(self):
        return self._list[0]


class Node():
    def __init__(self, index):
        self.conned_nodes = set()
        self.index = index
        self.visited = False

    def add_conned_node(self, Node):
        self.conned_nodes.add(Node)

    def get_unvisited_nodes(self):
        return sorted(
            [node for node in self.conned_nodes if not node.visited],
            key=lambda x: x.index
        )


def solve():
    N, M, start_node_index = map(int, sys.stdin.readline().split())
    node_dict = {}
    for i in range(N):
        node_dict[i + 1] = Node(i + 1)

    for i in range(M):
        from_node_index, to_node_index = map(int, sys.stdin.readline().split())
        from_node = node_dict[from_node_index]
        to_node = node_dict[to_node_index]
        from_node.add_conned_node(to_node)
        to_node.add_conned_node(from_node)

    # DFS
    dfs_result = []
    node_deq = DequeWoojin()
    node_deq.push_right(node_dict[start_node_index])

    while len(node_deq) > 0:
        node = node_deq.pop_left()
        if node.visited:
            continue
        dfs_result.append(node.index)
        node.visited = True
        next_nodes = node.get_unvisited_nodes()
        for i in range(len(next_nodes)):
            next_node = next_nodes[-i - 1]
            node_deq.push_left(next_node)
    print(*dfs_result)

    # BFS
    for i in range(N):
        node_dict[i + 1].visited = False
    bfs_result = []
    node_deq = DequeWoojin()
    node_deq.push_right(node_dict[start_node_index])
    while len(node_deq) > 0:
        node = node_deq.pop_left()
        if node.visited:
            continue
        bfs_result.append(node.index)
        node.visited = True
        next_nodes = node.get_unvisited_nodes()
        for i in range(len(next_nodes)):
            next_node = next_nodes[i]
            node_deq.push_right(next_node)
    print(*bfs_result)


def main():
    solve()


if __name__ == "__main__":
    main()
