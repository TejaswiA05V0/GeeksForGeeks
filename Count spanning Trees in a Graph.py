import numpy as np

class Solution:

    def countSpanTree(self, n, edges):

        # single node graph
        if n == 1:
            return 1

        lap = [[0] * n for _ in range(n)]

        for u, v in edges:
            # diagonal 
            lap[u][u] += 1
            lap[v][v] += 1
            # adjacency
            lap[u][v] -= 1
            lap[v][u] -= 1

        # remove last row & column
        cofactor = []
        for i in range(n - 1):
            row = []
            for j in range(n - 1):
                row.append(lap[i][j])

            cofactor.append(row)
        
        # note: In interview use Gaussian elimination to compute determinant efficiently
        return round(np.linalg.det(cofactor))
