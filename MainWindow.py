from tkinter import *
from Graph_db import graph, init_graph, write_to_file, connect_vertexes, save_ribs
import time

class MainWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Navigator")
        self.geometry("800x600")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.canvas = Canvas(self, bg='white')
        self.map = PhotoImage(file="Picture/Map.png")
        self.point = PhotoImage(file="Picture/Point.png")
        self.traffic = PhotoImage(file="Picture/traffic.png")
        self.canvas.grid(row=0, column=0, sticky='wsen')
        self.x = 0
        self.y = 0
        self.start = None
        self.finish = None
        self.dist = None

        self.traffic_jams_flag = False
        self.start_traffic_jams = []
        self.finish_traffic_jams = []
        self.traffic_jams_line = []

        self.bind("<Key>", self.button_pressed)
        self.bind("<Button-1>", self.set_traffic_points)
        self.bind("<Button-2>", self.clear_list_of_pares)
        self.bind("<Button-3>", self.find_path_from_to)
        self.list_of_pares = []
        init_graph()
        graph.create_adj_matrix()
        graph.init_traffic_jams()



    def clear_canvas(self):
        self.canvas.delete('all')


    def set_traffic_points(self, event):
        if not self.traffic_jams_flag:
            self.start_traffic_jams.append(graph.get_nearest_by_coordinates(event.x, event.y))
            self.traffic_jams_flag = True
        else:
            self.traffic_jams_line.clear()
            self.finish_traffic_jams.append(graph.get_nearest_by_coordinates(event.x, event.y))
            self.traffic_jams_flag = False
            n = len(self.finish_traffic_jams)
            graph.init_traffic_jams()
            for point in range(n):
                d = graph.A_star(self.start_traffic_jams[point].get_node(), self.finish_traffic_jams[point].get_node())
                d = d[self.finish_traffic_jams[point].get_node()][1]
                self.traffic_jams_line.append(d)
                graph.traffic_jams(d)
        self.render_path()

    def render_traffic_jams(self):
        for vert in self.start_traffic_jams:
            self.canvas.create_image(vert.get_x(), vert.get_y(), image=self.traffic, anchor='center')
        for vert in self.finish_traffic_jams:
            self.canvas.create_image(vert.get_x(), vert.get_y(), image=self.traffic, anchor='center')
        if self.finish_traffic_jams:
            self.render_traffic_line()

    def render_traffic_line(self):
        i = 0
        for temp in self.start_traffic_jams:
            temp2 = temp.get_coordinates()
            if i < len(self.traffic_jams_line):
                for node in self.traffic_jams_line[i]:
                    self.canvas.create_line(temp2, node.get_coordinates(), dash=(4, 2), width=2, fill='red')
                    temp2 = node.get_coordinates()
            i += 1

    def render_path(self):   ############################################################
        self.clear_canvas()
        self.canvas.create_image(self.x, self.y, image=self.map, anchor='nw')
        self.render_traffic_jams()
        if self.start:
            self.render_points_path()

    def render_points_path(self):
        vert = graph.get_nearest_by_coordinates(self.start.get_x(), self.start.get_y())
        self.canvas.create_image(vert.get_x(), vert.get_y(), image=self.point, anchor='center')
        if self.finish:
            self.render_line_path()
            self.canvas.create_image(self.finish.get_x(), self.finish.get_y(), image=self.point, anchor='center')

    def render_line_path(self):
        temp_coord = self.start.get_coordinates()
        for node in self.dist[self.finish.get_node()][1]:
            self.canvas.create_line(temp_coord, node.get_coordinates(), dash=(4, 2), width=3, fill='green')
            temp_coord = node.get_coordinates()

        """
        for vert in vertex.get_all_connected_vertexes():
            self.canvas.create_line(vertex.get_coordinates(), vert.get_coordinates())   ###################333333
        """
    def button_pressed(self, event):
        if event.keysym == "Left":
            if self.x < 0:
                self.x += 10
                graph.move_all_vertexes_x(10)
                self.render_path()
                print(self.x, self.y)
        elif event.keysym == "Right":
            if self.x > -2830:
                self.x -= 10
                graph.move_all_vertexes_x(-10)
                self.render_path()
                print(self.x, self.y)
        elif event.keysym == "Up":
            if self.y < 0:
                self.y += 10
                graph.move_all_vertexes_y(10)
                self.render_path()
                print(self.x, self.y)
        elif event.keysym == "Down":
            if self.y > -1010:
                self.y -= 10
                graph.move_all_vertexes_y(-10)
                self.render_path()
                print(self.x, self.y)


    def clear_list_of_pares(self, event):
        self.list_of_pares.clear()

    def find_path_from_to(self, event):
        if self.list_of_pares:
            self.list_of_pares.append(graph.get_nearest_by_coordinates(event.x, event.y))
            print(graph.get_nearest_by_coordinates(event.x, event.y).get_node(), '\n')  #flag
            self.dist = graph.A_star(self.list_of_pares[0].get_node(), self.list_of_pares[1].get_node())
            self.finish = self.list_of_pares[1]
            self.list_of_pares.clear()
        else:
            self.start = None
            self.finish = None
            self.render_path()
            print(graph.get_nearest_by_coordinates(event.x, event.y).get_node())  #flag
            self.list_of_pares.append(graph.get_nearest_by_coordinates(event.x, event.y))
            self.start = self.list_of_pares[0]
        self.render_path()


def main():
    root = MainWindow()
    root.render_path()
    root.mainloop()


if __name__ == '__main__':
    main()

"""   OLD needed code 
    def render_points(self, grph):
        for vert in grph.get_graph():
            self.canvas.create_image(vert.get_x(), vert.get_y(), image=self.point, anchor='center')
            self.render_line(vert)

    def render_line(self, vertex):
        for vert in vertex.get_all_connected_vertexes():
            self.canvas.create_line(vertex.get_coordinates(), vert.get_coordinates())

    def render_map(self):
        self.clear_canvas()
        self.canvas.create_image(self.x, self.y, image=self.map, anchor='nw')
        self.render_points(graph)
     
         def connect_vertexes(self, event):
        if self.list_of_pares:
            self.list_of_pares.append(graph.get_nearest_by_coordinates(event.x, event.y))
            connect_vertexes(self.list_of_pares[0], self.list_of_pares[1])
            print(graph.get_nearest_by_coordinates(event.x, event.y).get_node(), '\n')  #flag
            save_ribs(graph)
            self.list_of_pares.clear()
        else:
            print(graph.get_nearest_by_coordinates(event.x, event.y).get_node())  #flag
            self.list_of_pares.append(graph.get_nearest_by_coordinates(event.x, event.y))
        self.render_map()   
        
    def mouse_click_position(self, event):
        write_to_file(event.x + abs(self.x), event.y + abs(self.y))
        graph.add_vertex(event.x, event.y)
        print(event.x + abs(self.x), event.y + abs(self.y))

        """

"""   
    start_timer = time.time()
    for i in range(30):
       graph.dijkstra(2)
   print(time.time() - start_timer)
   start_timer = time.time()
   for i in range(30):
       graph.A_star(2, 67)
   print(time.time() - start_timer)"""