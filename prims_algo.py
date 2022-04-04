#O(N**2) Time Complexity 

class Graph:
    def __init__(self, num_of_nodes):
        self.m_num_of_nodes = num_of_nodes
        self.m_graph = [[0] for column in range(num_of_nodes) 
                            for row in range(num_of_nodes)]
    
    # add edge to adjacency matrix 
    def add_edge(self, node1, node2, weight): 
        self.m_graph[node1][node2] = weight
        self.m_graph[node2][node1] = weight 

    def prims_mst(self):
        pos_inf = float('inf')

        # list of visited nodes
        selected_nodes = [False for node in range(self.m_num_of_nodes)]

        result = [[0] for column in range(self.m_num_of_nodes)
                      for row in range(self.num_of_nodes)]

        index = 0 

        while (False in selected_nodes):
            minimum = pos_inf

            start = 0 

            end = 0 

            for i in range(self.m_num_of_nodes):
                if selected_nodes[i]:
                    for j in range(self.m_num_of_nodes): 
                        if not selected_nodes[j] and self.m_graph[i][j] > 0:
                            if self.m_graph[i][j] < minimum: 
                                minimum = self.m_graph[i][j]
                                start, end = i, j 
            
            selected_nodes[end] = True

            result[start][end] = minimum

            if minimum == pos_inf:
                result[start][end] = 0

            index += 1

            result[start][end] = result[end][start]

        for i in range(len(result)):
            for j in range(0+i, len(result)):
                if result[i][j] != 0:
                    print("%d - %d: %d" % (i, j, result[i][j]))