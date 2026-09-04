#Brute Force
from typing import List
class Solution:
    def maxsubarray(self, nums : List[int], k : int) -> int :
        n=len(nums)
        maxsum=0
        for i in range(0,n-k):
            sum=nums[i]
            for j in range(i+1,i+3):
                sum+=nums[j]
            
            maxsum=max(sum,maxsum)

        return maxsum  

df=Solution()
print(df.maxsubarray([2,9,31,-4,21,7], 3))  

# Optimal
from typing import List
class Solution:
    def maxsubarray(self, nums : List[int], k : int) -> int :
        n=len(nums)
        maxsum=0
        windowsum=0
        j=k
        for i in range(0,k):
            windowsum+=nums[i]
        maxsum=windowsum
        for p in range(1,n-k+1):
            windowsum-=nums[p-1]
            #print("first", windowsum)
            windowsum+=nums[j]
            #print("second", windowsum)
            maxsum=max(windowsum,maxsum)
            j+=1

        return maxsum  

df=Solution()
print(df.maxsubarray([2,9,31,-4,21,7], 3))  

# optimal 2
from typing import List
class Solution:
    def maxsubarray(self, nums : List[int], k : int) -> int :
        n=len(nums)
        window_sum = sum(nums[:k])
        maxsum=window_sum
        for i in range(k,n):
            window_sum+=nums[i]
            window_sum-=nums[i-k]
            maxsum=max(maxsum,window_sum)
        return maxsum

df=Solution()
print(df.maxsubarray([2,9,31,-4,21,7], 3))  
