class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
        return










































        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]

        for i in range(len(matrix)):
            # l,r=0,len(matrix)-1
            # while l<=r:
            #     matrix[i][r],matrix[i][l] = matrix[i][l],matrix[i][r]
            #     l+=1
            #     r-=1
            #matrix[i] = matrix[i][::-1]
            matrix[i].reverse()


        