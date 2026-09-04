

# ## 🧠 Core Idea

# You can flip **at most `k` zeros → ones**, so:

# 👉 You want the **longest subarray** that contains **at most `k` zeros**.

# ---

# ## 🔍 Strategy (Sliding Window)

# We maintain a window `[left, right]`:

# * Expand `right` → keep adding elements
# * Count how many `0`s are inside the window
# * If zeros exceed `k`, shrink from `left`
# * Track max window length

# ---

# ## ✅ Algorithm Steps

# 1. Initialize:

#    * `left = 0`
#    * `zero_count = 0`
#    * `max_len = 0`

# 2. Loop `right` from `0 → n-1`:

#    * If `nums[right] == 0`, increment `zero_count`
#    * While `zero_count > k`:

#      * If `nums[left] == 0`, decrement `zero_count`
#      * Move `left++`
#    * Update:

#      ```
#      max_len = max(max_len, right - left + 1)
#      ```

# ---

## 💻 Python Code
class Solution:


    def longestOnes(self,nums, k):
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_len = max(max_len, right - left + 1)
            print(max_len)

        return max_len
    
df=Solution()
print(df.longestOnes([1,1,1,0,0,0,1,1,1,1,0], k = 2))    


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        res = 0

        for num in nums:
            if num == 1:
                count += 1
                res = max(res, count)
            else:
                count = 0

        return res
# ```

# ---

# ## 🔎 Example Walkthrough

# ### Input:

# ```
# nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# ```

# * Window expands until it has >2 zeros
# * Then shrinks from left
# * Best window becomes:

# ```
# [1,1,1,0,0,1,1,1,1] → length = 6
# ```

# ---

# ## ⚡ Why This Works

# * You don’t actually flip zeros
# * You just **allow up to `k` zeros in window**
# * That *simulates flipping*

# ---

# ## ⏱ Complexity

# * Time: **O(n)** (each element visited at most twice)
# * Space: **O(1)**

# ---

# ## 🧠 Intuition in One Line

# 👉 *“Find the longest window with ≤ k zeros.”*

# ---

# If you want, I can show:

# * Dry run step-by-step (like interviewer expects)
# * Optimized variants
# * Similar problems (this pattern repeats a lot in interviews)
