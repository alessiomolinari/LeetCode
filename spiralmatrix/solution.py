import numpy as np
from typing import List

class Solution:
    action_sequence = ['R','D','L','U']
    action_moves = {
        'R': (0, 1),
        'D': (1, 0),
        'L': (-1, 0),
        'U': (-1, 0)
    }
    
     
    def initialize_visited(self, matrix: List[List[int]]) -> List[List[int]]:
        for i in matrix:
            for j in i:
                j = 0
        return matrix
    
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        matrix = np.array(matrix)
        visited = np.zeros(shape=matrix.shape)
        res = []
        #print(matrix)
        #print(visited)
                
        i = 0
        j = 0
        action_index = 0
        borders = (matrix.shape[0] - 1, matrix.shape[1] - 1 )
        
        res.append(matrix[0,0])
        print(0,0)
        visited[0, 0] = 1
        
        while not visited.all():

            inc_i, inc_j = self.action_moves[self.action_sequence[action_index]]
            i, j = i + inc_i, j + inc_j
            if i < matrix.shape[0] and j < matrix.shape[1]:
                if visited[i, j] == 0:
                    res.append(matrix[i, j])
                    print(i, j)
                    visited[i, j] = 1
                

            i, j = i - inc_i, j - inc_j
            action_index += 1
            print("new action index: ", self.action_sequence[action_index])
        
        return res.tolist()
        
        
        