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

    def find_bfs(self,source):
        self.f=[source]
        self.q=[source]
        print(self.f[0],end=" ")
        while len(self.f)!=self.v:
            try:
                n=(self.edges[self.q[0]])
                self.q.extend(list(n))
            except:
                n=self.q[0]
                self.q.extend(list(n))


            for i in n:
                if i not in self.f:
                    self.f.append(i)
                    print(i,end=" ")

            self.q.pop(0)






            #self.l.extend(list(self.edges[self.l[0]]))



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

s=input("Enter the Source Vertex:   ")
print("The BFS of the graph is : ")
g1.find_bfs(s)
