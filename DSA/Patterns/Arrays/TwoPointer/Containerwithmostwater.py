from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # calculate current area
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            max_area = max(max_area, area)

            # move the smaller height pointer
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

height = [1,8,6,2,5,4,8,3,7]
height=[1,1]
df=Solution()
ans=df.maxArea(height)
print(ans)