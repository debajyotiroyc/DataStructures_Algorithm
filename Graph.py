
class Graph():
    def __init__(self,v):
        self.v=v
        self.edges=dict()
    def add_edges(self,l):
        self.x, self.y = l.split()
        if self.x in self.edges.keys():
            self.edges[self.x].append(self.y)
        else:
            self.edges[self.x] = [self.y]

    def connected_vertices(self):
        for i,j in self.edges.items():
            j=str(",".join(map(str,j)))
            print(i,":",j)

v=int(input("Enter the number of vertices:  "))
g1=Graph(v)
i=0
while True:
    x=input("Enter the connected vertices: ")
    if x!="finish":
        g1.add_edges(x)
    else:
        break

print("All the connected vertices of this directed graph are:")
g1.connected_vertices()



