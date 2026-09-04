class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        sublength=0
        sum=0
        maxcount=0
        for i in range(len(arr)):
            sum=0
            count=0
            sum=sum+arr[i]
            count+=1
            
            for j in range(i+1,len(arr)):
                sum=sum+arr[j]
                count=count+1
            
                if(sum==k):
                    maxcount=max(count,maxcount)
        return maxcount         
                
arr=[-5,8,-14,2,4,12]
k = -5
dp=Solution()
print(dp.longestSubarray(arr,k))                    
                    
##Optimal
class Solution:
    def longestSubarray(self, arr, k):
        prefix_sum = 0
        max_len = 0
        prefix_map = {}  # stores first index of each prefix_sum

        for i in range(len(arr)):
            prefix_sum += arr[i]

            # Case 1: subarray from 0..i itself equals k
            if prefix_sum == k:
                max_len = max(max_len, i + 1)

            # Case 2: subarray between some j..i equals k
            if prefix_sum - k in prefix_map:
                max_len = max(max_len, i - prefix_map[prefix_sum - k])

            # Store prefix_sum if not already stored (first occurrence)
            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i

        return max_len

dp=Solution()
print(dp.longestSubarray(arr,k))                        
                
#optimal if only positive numbers 
def longestSubarray(arr, k):
    left = 0
    current_sum = 0
    max_len = 0

    for right in range(len(arr)):
        current_sum += arr[right]   # expand window

    # shrink window if sum > k
        while current_sum > k and left <= right:
                current_sum -= arr[left]
                left += 1

        # check if window sum == k
        if current_sum == k:
                max_len = max(max_len, right - left + 1)
    return max_len
   
dp=Solution()
print(dp.longestSubarray(arr,k))                  
        
