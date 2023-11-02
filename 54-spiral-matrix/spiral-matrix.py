# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         result = []
#         left, right = 0, len(matrix[0])
#         top, down = 0, len(matrix)
#         while left < right and top < down:
#             for i in range(left, right):
#                 result.append(matrix[top][i])
#             top += 1
#             for i in range(top, down):
#                 result.append(matrix[i][right - 1])
#             right -= 1
#             if not (left < right and top < down):
#                 break
#             for i in range(right - 1, left - 1, -1):
#                 result.append(matrix[down - 1][i])
#             down -= 1
#             for i in range(down - 1, top - 1, -1):
#                 result.append(matrix[i][left])
#             left += 1
#         return result
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        l, r = 0, len(matrix[0])
        t, b = 0, len(matrix)
        while t < b and l < r:
            # l --> r
            for i in range(l, r):
                result.append(matrix[t][i])
            t += 1
            for i in range(t, b):
                result.append(matrix[i][r - 1])
            r -= 1
            if not (l < r and t < b):
                break
            for i in range(r - 1, l - 1, -1):
                result.append(matrix[b - 1][i])
            b -= 1
            for i in range(b - 1, t - 1, -1):
                result.append(matrix[i][l])
            l += 1

        return result

    # def spiralOrder(self, matrix: List[List[int]]) -> List[int]:            
    #     result = []
    #     while matrix:
    #         result.extend(matrix.pop(0))
    #         matrix = [*zip(*matrix)][::-1]
    #     return result
