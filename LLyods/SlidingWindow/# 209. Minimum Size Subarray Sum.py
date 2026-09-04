from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        res_len=float('inf')
        c_sum=0
        for right in range(0,len(nums)):
            c_sum+=nums[right]
            while c_sum>=target:
                res_len=min(res_len,right-left+1)
                c_sum-=nums[left]
                left+=1          
        return res_len if res_len!=float('inf') else 0            
