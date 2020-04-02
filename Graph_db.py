from Graph import Graph, Vertex, graph, connect_vertexes, single_connection


def write_to_file(x, y):
    file = open('db.txt', 'a')
    file.write(str(x) + "," + str(y) + "\n")
    file.close()

def init_graph():
    file = open('db.txt', 'r')
    for line in file.readlines():
        x = int(line.split(',')[0])
        y = int(line.split(',')[1])
        graph.add_vertex(x, y)
    file.close()
    file = open('ribs_db.txt', 'r')
    for line in file.readlines():
        connected_vertexes = []
        new_line = rewrite_line(line)
        splited_array = new_line.split(',')
        for spl in splited_array:
            if spl.isdigit():
                connected_vertexes.append(int(spl))
        for i in range(1, len(connected_vertexes)):
            single_connection(graph.get_vertex_by_id(connected_vertexes[0]), graph.get_vertex_by_id(connected_vertexes[i]))
        print(connected_vertexes)

def save_ribs(graph):
    file = open('ribs_db.txt', 'w')
    for vertex in graph.get_graph():
        file.write(str(vertex.get_node()) + "," + str(vertex.get_all_connected_vertexes_by_id()) + "\n")
    file.close()

def rewrite_line(str):
    str = str.replace('[', '')
    str = str.replace(' ', '')
    str = str.replace(']', '')
    str = str.replace('\n', '')
    return str