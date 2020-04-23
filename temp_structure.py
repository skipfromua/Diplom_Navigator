class QueueNode:
    def __init__(self, node, priority):
        self.node = node
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.list_of_nodes = []

    def pop(self):
        return self.list_of_nodes.pop(0)

    def push(self, node, priority):
        if self.list_of_nodes:
            for i in range(len(self.list_of_nodes)):
                if self.list_of_nodes[i].priority > priority:
                    self.list_of_nodes.insert(i, QueueNode(node, priority))
                    return
            self.list_of_nodes.append(QueueNode(node, priority))
        else:
            self.list_of_nodes.append(QueueNode(node, priority))

    def show(self):
        for node in self.list_of_nodes:
            print(node.node, node.priority)


####################################################################################


class Node:
    def __init__(self, name):
        self.name = name
        self.neighbours = []


class Graph:
    def __init__(self):
        self.list_of_nodes = []
        self.adj_matrix = []

    def add_node(self, name):
        self.list_of_nodes.append(Node(name))

    def connect(self, node1, node2, distance):
        node1 = self.get_node_by_name(node1)
        node2 = self.get_node_by_name(node2)
        self.list_of_nodes.index(node1)
        for node in self.list_of_nodes:
            if node.name == node1.name:
                node.neighbours.append(node2)
            elif node.name == node2.name:
                node.neighbours.append(node1)
        for i in range(len(self.list_of_nodes)):
            for j in range(len(self.list_of_nodes)):
                if self.list_of_nodes.index(node1) == i and self.list_of_nodes.index(node2) == j \
                        or self.list_of_nodes.index(node1) == j and self.list_of_nodes.index(node2) == i:
                    self.adj_matrix[i][j] = distance

    def init_adj_matrix(self):
        temp = []
        for i in range(len(self.list_of_nodes)):
            for j in range(len(self.list_of_nodes)):
                temp.append(0)
            self.adj_matrix.append(temp)
            temp = []

    def get_node_by_name(self, name):
        for node in self.list_of_nodes:
            if name == node.name:
                return node

    def get_distance(self, node1, node2):
        for i in range(len(self.list_of_nodes)):
            for j in range(len(self.list_of_nodes)):
                if self.list_of_nodes.index(node1) == i and self.list_of_nodes.index(node2) == j \
                        or self.list_of_nodes.index(node1) == j and self.list_of_nodes.index(node2) == i:
                    return self.adj_matrix[i][j]

    def Dijkstra(self, start, finish):
        start = self.get_node_by_name(start)
        finish = self.get_node_by_name(finish)
        queue = PriorityQueue()
        for node in start.neighbours:
            queue.push(node, self.get_distance(start, node))
        seen = [{start: 0}]
        answer = [start]
        while queue.list_of_nodes:
            node = queue.pop().node
            for next in node.neighbours:
                queue.push(next, self.get_distance(node, next))
                if next.name == finish.name or not self.in_seen(next.name, seen):
                    v = list(seen[-1].values())[0]
                    seen.append({next: v + self.get_distance(node, next)})
                    answer.append(next)
        return seen

    @staticmethod
    def in_seen(name, seen):
        for element in seen:
            if name in list(element.keys()):
                return True
        return False

g = Graph()
g.add_node('a')
g.add_node('b')
g.add_node('c')
g.add_node('d')
g.add_node('e')
g.add_node('f')
g.init_adj_matrix()
g.connect('a', 'b', 3)
g.connect('a', 'c', 2)
g.connect('b', 'd', 4)
g.connect('b', 'f', 6)
g.connect('e', 'c', 7)
g.connect('d', 'c', 5)
g.connect('d', 'e', 1)
g.connect('e', 'a', 9)
a = g.Dijkstra('f', 'e')
print(a)
# g.Dijkstra('a')
