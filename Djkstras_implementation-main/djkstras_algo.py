import heapq


class Vertex:
    def __init__(self, v, cost, color, edges):
        self.v = v
        self.edges = edges
        self.color = color
        self.cost = cost

    def __lt__(self, other_vertex):
        return self.cost < other_vertex.cost


class Djkstras:
    def findShortestPath(self, source, destination, graph):
        vertexes = {}
        q = [] 
        result = {}
        for k, v in graph.items():
            ver = Vertex(k, float('inf'), "WHITE", v)
            vertexes[k] = ver
        
        heapq.heappush(q, vertexes[source])
        ver = vertexes[source]
        ver.color = "GRAY"
        ver.cost = 0
        
        ## See if all the vertextes are white initially
        for k, val in vertexes.items():
            print(val.v, val.color, val.cost, val.edges)

        while q:
            curr_vertex = heapq.heappop(q)
            curr_cost = curr_vertex.cost
            neighbours = curr_vertex.edges
            
            for edge in neighbours:
                # edge[0] is the neighbour (v) and edge[1] is the distance
                v = vertexes[edge[0]]
                
                if  curr_cost + edge[1] < v.cost:
                    v.cost = edge[1] + curr_cost
                    result[edge[0]] = curr_vertex.v

                    if v.color == "WHITE":
                        v.color = "GRAY" 
                        heapq.heappush(q, v)
                    elif v.color == "GRAY":
                        # Need to implement decrement_key
                        heapq.heappush(q, v)
                
                
            curr_vertex.color = "BLACK"
        
        ## See if all the vertextes are BLACK in the end
        for k, val in vertexes.items():
            print(val.v, val.color, val.cost, val.edges)

        return result
                


d = Djkstras()
print(d.findShortestPath(0, 5,  {0:[[1, 2], [2, 5]], 1:[[2, 8], [4, 7]], 2:[[3, 4], [4, 2]], 3:[[4, 6], [5, 3]], 4:[[5, 1]], 5:[]}))