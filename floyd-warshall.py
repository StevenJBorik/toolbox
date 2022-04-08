# All pairs shortest path algorithm
INF = 99999
def floydWarshall(graph,n): #n=no. of vertex
    dist=graph
    for k in range(n):
        for i in range(n):
            for j in range(n): 
                dist[i][j] = min(dist[i][j], dist[i][k]+ dist[k][j])
    return dist