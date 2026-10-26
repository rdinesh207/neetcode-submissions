class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rz = False
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                if not matrix[r][c]:
                    matrix[0][c]=0
                    if r>0:
                        # print(r)
                        matrix[r][0]=0
                    else:
                        rz = True
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c]==0 or matrix[r][0]==0:
                    matrix[r][c]=0
        
        if matrix[0][0]==0:
            for r in range(rows):
                matrix[r][0]=0
        if rz:
            for c in range(cols):
                matrix[0][c]=0


        
        
        