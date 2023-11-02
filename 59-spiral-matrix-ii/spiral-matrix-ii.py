class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for i in range(n)]
        left, right=0,len(matrix)
        top,bottom = 0,len(matrix)
        x=1
        while left<right and top<bottom:
            for i in range(left,right):
                matrix[top][i] = x
                x+=1
            top+=1
            for i in range(top,bottom):
                matrix[i][right-1] =x
                x+=1
            right-=1
            if not(left<right and top<bottom):
                break
            for i in range(right-1,left-1,-1):
                matrix[bottom-1][i] =x
                x+=1
            bottom-=1
            for i in range(bottom-1,top-1,-1):
                matrix[i][left]=x
                x+=1
            left+=1
        return matrix