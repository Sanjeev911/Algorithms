from graphs import directed_graph
from graphs import Vertex
max_number = 9999999
class Priority():
    def __init__(self,graph =None):
        if graph == None:
            self.queue = {}
            self.dist_list = []
        else:
            self.queue = dict((vertex,max_number) for vertex in graph.vertices)
            self.dist_list = []
    def add(self,tup):
        self.queue[tup[0]] = tup[1]
        self.dist_list = sorted(self.queue.items(),key = lambda kv:kv[1])

    def pop(self):
        if len(self.dist_list)>0:
            a = self.dist_list[0]
            del self.dist_list[0]
            self.queue.__delitem__(a[0])
            return a
        return None



def djikstra(graph,source,destination):
    distances = Priority(graph)
    output ={}
    visited = {}
    source_vertex = graph.find(source)
    destination_vertex = graph.find(destination)
    distances.add((source_vertex,0))
    while(len(distances.dist_list)>0):        
        vertex,dist = distances.pop()
        visited[vertex] = True
        for neighbour in vertex.neighbours:
            if neighbour not in visited:
                if distances.queue[neighbour[0]] >= (dist + neighbour[1]):
                    distances.add((neighbour[0],dist + neighbour[1]))
                    output[neighbour[0]] = dist + neighbour[1]
    return output



g=directed_graph(4)
g.add_edge(0, 1, 1)
g.add_edge(1, 2, 2)
g.add_edge(0, 2, 4)
g.add_edge(2, 3, 5)

g.plot()

output = djikstra(g,0,3)
print(output[g.find(2)])
