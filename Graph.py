import math
from myQueue import Queue
from myQueue import PriorityQueue

inf = 999999999

class Vertex:
    def __init__(self, x, y, id):
        self.__x = x
        self.__y = y
        self.__id = id
        self.__connected_vertexes = []

    def add_vertex(self, vertex):
        self.__connected_vertexes.append(vertex)

    def get_all_connected_vertexes(self):
        return self.__connected_vertexes

    def get_all_connected_vertexes_by_id(self):
        ids_of_vertexes = []
        for vertexes in self.__connected_vertexes:
            ids_of_vertexes.append(vertexes.get_node())
        return ids_of_vertexes


    def show_all_connected_vertexes(self):
        print(self.__connected_vertexes)

    def get_coordinates(self):
        return self.__x, self.__y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_node(self):
        return self.__id

    def move_x(self, dx):
        self.__x += dx

    def move_y(self, dy):
        self.__y += dy


def connect_vertexes(v1, v2):  # this function add oriented rib
    v1.add_vertex(v2)
    v2.add_vertex(v1)


def single_connection(v1, v2):
    v1.add_vertex(v2)


class Graph:
    __number_vertexes = 0
    __list_of_vertexes = []

    def create_adj_matrix(self):
        self.adj_mat = [[0] * len(self.__list_of_vertexes) for _ in range(len(self.__list_of_vertexes))]
        for node in self.__list_of_vertexes:
            for to_node in self.__list_of_vertexes:
                if to_node in node.get_all_connected_vertexes():
                    self.adj_mat[node.get_node()][to_node.get_node()] = \
                        pow((pow((node.get_x()-to_node.get_x()), 2) + pow((node.get_y()-to_node.get_y()), 2)), 1/2)

    def add_vertex(self, x, y):
        self.__number_vertexes += 1
        self.__list_of_vertexes.append(Vertex(x, y, len(self.__list_of_vertexes)))

    def get_graph(self):
        return self.__list_of_vertexes

    def move_all_vertexes_x(self, dx):
        for i in self.__list_of_vertexes:
            i.move_x(dx)

    def move_all_vertexes_y(self, dy):
        for i in self.__list_of_vertexes:
            i.move_y(dy)

    def get_vertex_by_id(self, id):
        for i in self.__list_of_vertexes:
            if i.get_node() == id:
                return i

    def neighbors(self, node):
        return node.get_all_connected_vertexes()

    def cost(self, start, goal):
        return pow((pow((start.get_x()-goal.get_x()), 2) + pow((start.get_y()-goal.get_y()), 2)), 1/2)

    def get_nearest_by_coordinates(self, x, y):
        min_range = math.sqrt(abs(self.__list_of_vertexes[0].get_x() - x)**2 + abs(self.__list_of_vertexes[0].get_y() - y)**2)
        looking_node = self.__list_of_vertexes[0]
        for i in self.__list_of_vertexes:
            if min_range > math.sqrt(abs(i.get_x() - x)**2 + abs(i.get_y() - y)**2):
                min_range = math.sqrt(abs(i.get_x() - x)**2 + abs(i.get_y() - y)**2)
                looking_node = i
        return looking_node

    def connections_from(self, node):
        return [(self.__list_of_vertexes[col_num], self.adj_mat[node][col_num]) for col_num in range(len(self.adj_mat[node])) if
                self.adj_mat[node][col_num] != 0]

    def dijkstra(self, node):
        # Получает индекс узла (или поддерживает передачу int)
        nodenum = self.get_vertex_by_id(node).get_node()
        dist = [None] * len(self.__list_of_vertexes)
        for i in range(len(dist)):
            dist[i] = [float('inf')]
            dist[i].append([self.__list_of_vertexes[nodenum]])

        dist[nodenum][0] = 0
        # Добавляет в очередь все узлы графа
        # Отмечает целые числа в очереди, соответствующие индексам узла
        # локаций в массиве self.nodes
        queue = [i for i in range(len(self.__list_of_vertexes))]
        # Набор увиденных на данный момент номеров
        seen = set()
        while len(queue) > 0:
            # Получает узел в очереди, который еще не был рассмотрен
            # и который находится на кратчайшем расстоянии от источника
            min_dist = inf
            min_node = None
            for n in queue:
                if dist[n][0] < min_dist and n not in seen:
                    min_dist = dist[n][0]
                    min_node = n

            # Добавляет мин. расстояние узла до увиденного, убирает очередь
            queue.remove(min_node)
            seen.add(min_node)
            # Получает все следующие перескоки
            connections = self.connections_from(min_node)
            # Для каждой связи обновляет путь и полное расстояние от
            # исходного узла, если полное расстояние меньше
            # чем текущее расстояние в массиве dist
            for (node, weight) in connections:
                tot_dist = weight + min_dist
                if tot_dist < dist[node.get_node()][0]:
                    dist[node.get_node()][0] = tot_dist
                    dist[node.get_node()][1] = list(dist[min_node][1])
                    dist[node.get_node()][1].append(node)
        return dist

    def heuristic(self, a, b):
        (x1, y1) = a.get_x(), a.get_y()
        (x2, y2) = b.get_x(), b.get_y()
        return abs(x1 - x2) + abs(y1 - y2)

    def A_star(self, node, goal):
        nodenum = self.get_vertex_by_id(node).get_node()
        dist = [None] * len(self.__list_of_vertexes)
        for i in range(len(dist)):
            dist[i] = [float('inf')]
            dist[i].append([self.__list_of_vertexes[nodenum]])
        dist[nodenum][0] = 0
        queue = [i for i in range(len(self.__list_of_vertexes))]
        seen = set()
        while len(queue) > 0:
            min_dist = inf
            min_node = None
            for n in queue:
                if dist[n][0] < min_dist and n not in seen:
                    min_dist = dist[n][0]
                    min_node = n
            queue.remove(min_node)
            seen.add(min_node)
            connections = self.connections_from(min_node)
            for (node, weight) in connections:
                tot_dist = weight + min_dist + self.heuristic(self.get_vertex_by_id(min_node), node)
                if tot_dist < dist[node.get_node()][0]:
                    dist[node.get_node()][0] = tot_dist
                    dist[node.get_node()][1] = list(dist[min_node][1])
                    dist[node.get_node()][1].append(node)
            if self.get_vertex_by_id(min_node).get_node() == self.get_vertex_by_id(goal).get_node():
                return dist
        return dist

graph = Graph()
