import matplotlib.pyplot as plt
import random

def plot_graph(graph):
    a = [i for i in range (10,20+graph.total_vertices)]
    b= [i for i in range (1,30+graph.total_vertices)]
    x = random.sample(a,graph.total_vertices)
    y = random.sample(b,graph.total_vertices)
    vertices = graph.vertices
    for i,vertex in enumerate(vertices):
        plt.scatter(x[i],y[i],color = "black",s = 100)
        plt.text(x[i]+0.3,y[i]+0.3,vertex.value,fontsize = 9)
        vertex.x,vertex.y = x[i],y[i]
    for edge in graph.edges:
        plt.plot([edge[0].x,edge[1].x],[edge[0].y,edge[1].y])
    plt.show()

class one_edge:
        def __init__(self,vertex1,vertex2,weight):
            self.source = vertex1
            self.destination = vertex2
            self.weights = weight
class Vertex:
    def __init__(self,value):
        self.value = value
        self.neighbours = []
        self.x = 0
        self.y = 0

class directed_graph:
    def __init__(self,value):
        self.total_vertices = value
        self.vertices = []
        self.vertices_values = []
        self.edges =[]

    def find(self,val):
        for i in self.vertices:
            if i.value == val:
                v = i
                break
        return v


    def add_edge(self,vertex1,vertex2):
        for i in [vertex1,vertex2]:
            if i not in self.vertices_values:
                self.vertices.append(Vertex(i))
                self.vertices_values.append(i)
        v1 = self.find(vertex1)
        v2 = self.find(vertex2)
        v1.neighbours.append(v2)
        self.edges.append([v1,v2])


    def info(self):
        print("Total no.of vertices = ",self.total_vertices)
        print(" List of vertices values = ",self.vertices_values)
        for i in self.vertices:
            print(i,i.neighbours)

    def plot(self):
        plot_graph(self)
        pass

    def BFS(self,val):
        print("Breadth-First-Traversal of the directed tree from node "+str(val) +" is as:")
        visited = []
        queue = []
        start = self.find(val)
        queue.append(start)
        while(queue):
            v = queue.pop(0)
            if v.value not in visited:
                visited.append(v.value)
                print(v.value , end = " ")
                for i in v.neighbours:
                    queue.append(i)
        return

    def DFS(self,val):
        print("Depth-First-Traversal of the directed tree from node "+str(val) +" is as:")
        visited = []
        queue = []
        start = self.find(val)
        queue.append(start)
        while(queue):
            v = queue.pop()
            if v.value not in visited:
                visited.append(v.value)
                print(v.value , end = " ")
                for i in v.neighbours:
                    queue.append(i)
        return

class undirected_graph:
    def __init__(self,value):
        self.total_vertices = value
        self.vertices = []
        self.vertices_values = []
        self.edges =[]

    def find(self,val):
        for i in self.vertices:
            if i.value == val:
                v = i
                break
        return v


    def add_edge(self,vertex1,vertex2):
        for i in [vertex1,vertex2]:
            if i not in self.vertices_values:
                self.vertices.append(Vertex(i))
                self.vertices_values.append(i)
        v1 = self.find(vertex1)
        v2 = self.find(vertex2)
        v1.neighbours.append(v2)
        v2.neighbours.append(v1)
        self.edges.append([v1,v2])

    def info(self):
        print("Total no.of vertices = ",self.total_vertices)
        print(" List of vertices values = ",self.vertices_values)
        for i in self.vertices:
            print(i,i.neighbours)

    def plot(self):
        plot_graph(self)
        pass

    def BFS(self,val):
        print("Breadth-First-Traversal of the undirected tree from node "+str(val) +" is as:")
        visited = []
        queue = []
        start = self.find(val)
        queue.append(start)
        while(queue):
            v = queue.pop(0)
            if v.value not in visited:
                visited.append(v.value)
                print(v.value , end = " ")
                for i in v.neighbours:
                    queue.append(i)

        return
    def DFS(self,val):
        print("Depth-First-Traversal of the undirected tree from node "+str(val) +" is as:")
        visited = []
        queue = []
        start = self.find(val)
        queue.append(start)
        while(queue):
            v = queue.pop()
            if v.value not in visited:
                visited.append(v.value)
                print(v.value , end = " ")
                for i in v.neighbours:
                    queue.append(i)
        return


if __name__=='__main__':
    g=directed_graph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(0, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    g.BFS(2)
    g.plot()
    print()


    f = undirected_graph(6)
    f.add_edge(1,2)
    f.add_edge(1,3)
    f.add_edge(2,4)
    f.add_edge(2,5)
    f.add_edge(4,5)
    f.add_edge(4,6)
    f.add_edge(3,5)
    f.add_edge(5,6)
    f.DFS(1)
    f.plot()
