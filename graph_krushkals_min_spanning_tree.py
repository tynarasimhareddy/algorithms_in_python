#python 3.x
class Graph:
    def __init__(self, n):
        self.V = n
        self.E = []
        self.parent = [i for i in range(self.V)]
        self.rank = [0 for i in range(self.V)]

    def addEdge(self, u, v, w):
        self.E.append([u,v,w])

    def find(self, e):
        if self.parent[e] == e:
            return e
        return self.find(self.parent[e])

    def union(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)

        if self.rank[p_x] < self.rank[p_y]:
            self.parent[p_x] = p_y
        elif self.rank[p_y] < self.rank[p_x]:
            self.parent[p_y] = p_x
        else:
            self.parent[p_x] = p_y
            self.rank[p_y] += 1

    def krushkal_algo(self):
        # sort the edges based on their weight
        self.E = sorted(self.E, key=lambda e:e[2])
        result = []
        # evaluate every edge in increasing weight order and add to result if it does not form a cycle
        for edge in self.E:
            p_u = self.find(edge[0])
            p_v = self.find(edge[1])
            if p_u != p_v:
                result.append(edge)
                self.union(edge[0], edge[1])

        print("Following are the edges of Minimum spanning tree")
        for e in result:
            print("{} ===> {} = {}".format(*e))
        
        return result

g = Graph(4)
g.addEdge(0, 1, 10) 
g.addEdge(0, 2, 6) 
g.addEdge(0, 3, 5) 
g.addEdge(1, 3, 15) 
g.addEdge(2, 3, 4)

g.krushkal_algo()

        
