from typing import List
# height = [4,2,0,3,2,5]
# class Solution:
#     def left_height(self,c_building,height):
#         r=c_building-1
#         max_height=0
#         while r>=0:
            
#             max_height=max(max_height,height[r])
#             r=r-1
#         return max_height
#     def right_height(self,c_building,height):
#         r=c_building+1
#         max_height=0
#         while r<len(height):
            
#             max_height=max(max_height,height[r])
#             r=r+1
#         return max_height   
#     def trap(self, height: List[int]) -> int:

#         c_sum=0
#         liss=[]
#         for i in range(0,len(height)):
#             left=self.left_height(i,height)
#             #print("left",left,"i",height[i])
#             right=self.right_height(i,height)
#             #print("right",right,"i",height[i])
#             min_height=min(left,right)
#             min_height=min_height-height[i]
#             area=1*min_height
#             #print("area",area)
#             liss.append(area)
           
#             if(area>0):
#              c_sum=c_sum+area
#         #print(liss)     
#         return c_sum
    
# df=Solution()
# print(df.trap(height))



from typing import List

height = [4, 2, 0, 3, 2, 5]

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        prefix_max = [0] * n
        suffix_max = [0] * n

        # Prefix max (left to right)
        prefix_max[0] = height[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], height[i])

        # Suffix max (right to left)
        suffix_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            suffix_max[i] = max(suffix_max[i+1], height[i])

        # Calculate trapped water
        total = 0
        for i in range(n):
            total += min(prefix_max[i], suffix_max[i]) - height[i]

        return total


df = Solution()
print(df.trap(height))  # ✅ Output: 9

#optimal

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        left_max, right_max = 0, 0
        total = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total += right_max - height[right]
                right -= 1

        return total


height = [4,2,0,3,2,5]
df = Solution()
print(df.trap(height))  # ✅ Output: 9


# This is **Trapping Rain Water** — harder than Container With Most Water because **water is trapped between bars**, not edges.

# I’ll explain **brute force → better → optimal**, with **math + intuition**, exactly how interviewers want.

# ---

# ## 🧠 Problem in plain English

# You’re given heights:

# ```
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# ```

# Bars have width = 1.

# Water is trapped **between bars**, not on edges.

# ---

# ## 🔢 Core formula (IMPORTANT)

# Water trapped at index `i`:

# [
# \text{water}[i] = \max(0,\ \min(\text{maxLeft}_i,\ \text{maxRight}_i) - height[i])
# ]

# Total water = sum of all `water[i]`.

# ---

# # 🔴 1️⃣ Brute Force Approach

# ### Idea

# For every index:

# * Find the **maximum bar on the left**
# * Find the **maximum bar on the right**
# * Compute water

# ---

# ## 🧑‍💻 Brute force code

# ```python
# class Solution:
#     def trap(self, height):
#         n = len(height)
#         total = 0

#         for i in range(n):
#             left_max = max(height[:i+1])
#             right_max = max(height[i:])

#             water = min(left_max, right_max) - height[i]
#             if water > 0:
#                 total += water

#         return total
# ```

# ---

# ## ⏱️ Complexity

# * Time: **O(n²)**
#   (`max()` inside loop)
# * Space: **O(1)**

# ❌ Too slow for large input.

# ---

# # 🟡 2️⃣ Better Approach (Prefix arrays)

# ### Idea

# Precompute:

# * `leftMax[i]`
# * `rightMax[i]`

# ---

# ## 🧑‍💻 Code

# ```python
# class Solution:
#     def trap(self, height):
#         n = len(height)
#         if n == 0:
#             return 0

#         leftMax = [0] * n
#         rightMax = [0] * n

#         leftMax[0] = height[0]
#         for i in range(1, n):
#             leftMax[i] = max(leftMax[i-1], height[i])

#         rightMax[n-1] = height[n-1]
#         for i in range(n-2, -1, -1):
#             rightMax[i] = max(rightMax[i+1], height[i])

#         total = 0
#         for i in range(n):
#             total += min(leftMax[i], rightMax[i]) - height[i]

#         return total
# ```

# ---

# ## ⏱️ Complexity

# * Time: **O(n)**
# * Space: **O(n)**

# Good but not optimal space.

# ---

# # 🟢 3️⃣ Optimal Approach — Two Pointers (INTERVIEW GOLD)

# ### 🔑 Key Insight

# Water trapped depends on the **smaller boundary**.

# Same idea as Container With Most Water, but **applied per index**.

# ---

# ## Algorithm

# * Two pointers: `left`, `right`
# * Track:

#   * `leftMax`
#   * `rightMax`
# * Move the pointer with **smaller height**

# ---

# ## 🧑‍💻 Optimal code

# ```python
# class Solution:
#     def trap(self, height):
#         left, right = 0, len(height) - 1
#         leftMax, rightMax = 0, 0
#         total = 0

#         while left < right:
#             if height[left] < height[right]:
#                 leftMax = max(leftMax, height[left])
#                 total += leftMax - height[left]
#                 left += 1
#             else:
#                 rightMax = max(rightMax, height[right])
#                 total += rightMax - height[right]
#                 right -= 1

#         return total
# ```

# ---

# ## ⏱️ Complexity (BEST POSSIBLE)

# * Time: **O(n)**
# * Space: **O(1)** ✅

# ---

# ## 🔍 Why moving smaller pointer works (math intuition)

# If:
# [
# height[left] < height[right]
# ]

# Then:
# [
# \min(\text{leftMax}, \text{rightMax}) = \text{leftMax}
# ]

# So water at `left` depends only on `leftMax`.

# Right side is guaranteed to be taller.

# ---

# ## 📌 Example

# For:

# ```
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# ```

# Total trapped water = **6**

# ---

# ## 🧠 Final comparison table

# | Approach    | Time  | Space | Interview |
# | ----------- | ----- | ----- | --------- |
# | Brute Force | O(n²) | O(1)  | ❌         |
# | Prefix Max  | O(n)  | O(n)  | 🟡        |
# | Two Pointer | O(n)  | O(1)  | ✅         |

# ---

# ## 🎯 One-line interview explanation

# > “At each step, water trapped depends on the smaller boundary, so we move that pointer and accumulate water.”

# ---

# If you want next:

# * Full dry-run with numbers
# * Why this problem is harder than Container With Most Water
# * Stack-based solution (another pattern)

# Just say.
