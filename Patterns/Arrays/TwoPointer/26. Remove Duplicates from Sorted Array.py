from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        i = 0  # points to last unique element
        
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:  # found a new unique element
                i += 1
                nums[i] = nums[j]
        
        return i + 1  # length = index + 1
nums=[1,1,2]
df=Solution()
ans=df.removeDuplicates(nums) 
print(ans)     
        