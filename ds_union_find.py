# Python Implementation for Union Find data structure

class UF:

    def __init__(self, N): 
        self.id = list(range(N))
        self.count = N
        self.rank = [0] * N 

    def find(self, p): 
        # Find the set identifier for item p #

        id = self.id
        while p != id[p]:
            # path compression 
            p = id[p] = id[id[p]]
        return p 
    
    def count(self):
        # return number of items 

        return self.count
    
    def connected(self, p, q):
        # Check if items p and q are on same set or not #

        return self.find(p) == self.find(q)
    
    def union(self, p, q): 
        # combine sets p and q into a single set # 

        id = self.id 
        rank = self.rank

        i = self.find(p)
        j = self.find(q)

        if i == j:
            return 
        
        self.count -= 1
        if rank[i] < rank[j]:
            id[i] = j 
        elif rank[j] < rank[i]: 
            id[j] = i
        else:
            id[j] = i 
            rank[i] += 1
    def __str__(self):
        # String representation of the union find object. #
        
        return " ".join([str(x) for x in self._id])

    def __repr__(self):
        
        # Representation of the union find object. #
        return "UF(" + str(self) + ")"


