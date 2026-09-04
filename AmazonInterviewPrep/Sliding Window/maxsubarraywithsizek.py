class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
      n=len(arr)
      left=0
      max_sum=0
      curr_sum=0
      for right in range(0,n):
          
          curr_sum+=arr[right]
          if((right-left+1)==k):
              max_sum=max(max_sum,curr_sum)
              curr_sum=curr_sum-arr[left]
              left+=1
      return max_sum          
              
              
          
        