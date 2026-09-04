from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]   # because problem says 1-indexed
            
            elif current_sum < target:
                left += 1    # need a bigger sum → move left pointer
            
            else:
                right -= 1   # need a smaller sum → move right pointer

numbers = [2,7,11,15]
target = 18
df=Solution()
ans=df.twoSum(numbers,target)  
print(ans)     
        










