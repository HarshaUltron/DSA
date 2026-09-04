matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#rint(len(matrix[0]))

breadth=len(matrix[0])
depth=len(matrix)

# print(breadth)

# print(depth)

class Solution:
    def spiralOrder(self, matrix):
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        print(top)
        print(bottom)
        print(left)
        print(right)
        while top <= bottom and left <= right:
            # 1. Traverse top row
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # 2. Traverse right column
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # 3. Traverse bottom row
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            # 4. Traverse left column
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res

df=Solution()

print(df.spiralOrder(matrix))