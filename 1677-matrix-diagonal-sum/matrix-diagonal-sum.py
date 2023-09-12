class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum =0
        # for i in range(len(mat)):
        #     for j in range(len(mat)):
        #         if i ==j:
        #             sum+=mat[i][j]
        #         if i+j == len(mat)-1:
        #             sum+= mat[i][j]
        # if len(mat) % 2 ==1:
        #     sum -= mat[len(mat)//2][len(mat)//2]

        for i in range(len(mat)):
            sum+=mat[i][i]
            if i != len(mat)-i-1:
                sum+=mat[i][len(mat)-i-1]
        # if len(mat) % 2 ==1:
        #     sum -= mat[len(mat)//2][len(mat)//2]
        return sum