class Solution:
 def maxArea(self, mat):
    n = len(mat)
    m = len(mat[0])

    ans = 0
    height = [0] * m

    for i in range(n):

        # Update heights
        for j in range(m):
            if mat[i][j] == 1:
                height[j] = height[j] + 1
            else:
                height[j] = 0

        # Sort columns by height
        h = sorted(height, reverse=True)

        # Calculate maximum area
        for j in range(m):
            area = h[j] * (j + 1)

            if area > ans:
                ans = area

    return ans          it is hard but you ll'try with using this logic is best for you man!
