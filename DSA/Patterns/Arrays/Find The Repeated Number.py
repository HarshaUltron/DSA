from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        d = {i: 0 for i in range(1, n+1)}
        for i in nums:
            if d.get(i,0)==0:
                d[i]+=1
            else:
                return i    

df=Solution()
#print(df.findDuplicate(nums = [8,1,1,1,2,7,4,3,1,1]))

# Optimal Solution (Floyd’s Tortoise and Hare cycle detection)

# This is the standard LeetCode #287: Find the Duplicate Number optimal approach.

# ✅ Time: O(n)
# ✅ Space: O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        
        # Phase 1: Detect cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        print(slow)
        # Phase 2: Find entrance to the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

df=Solution()
print(df.findDuplicate(nums = [8,1,1,1,2,7,4,3,1,1]))
#✅ This uses the cycle detection idea (like Linked List cycle) — because the array can be visualized as a graph where each index points to another index.