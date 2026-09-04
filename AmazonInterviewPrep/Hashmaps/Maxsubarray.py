from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum=float('-inf')
        current_sum=0
        
        for i in range(0,n):
            current_sum+=nums[i]
            if current_sum<0:
                max_sum=max(max_sum,current_sum)
                current_sum=0
            max_sum=max(max_sum,current_sum)    


        return max_sum

df=Solution()
print(df.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))       




class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        max_sum = float('-inf')
        current_sum = 0
        #subarr = []

        for i in range(n):
            #subarray = []
               
    
                if current_sum+nums[i]<nums[i]:
                   current_sum=nums[i]
                else:
                    current_sum += nums[i]
                #subarray.append(nums[end])
                if current_sum > max_sum:
                    max_sum = current_sum
                    #subarr = subarray[:]   # <-- make a copy

        return max_sum            
    


from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum
