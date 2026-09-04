def findMaxConsecutiveOnes(nums):
    count = 0
    max_count = 0
    
    for num in nums:
        if num == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0  # reset if 0 found
    return max_count

arr = [1,1,0,1,1,1,0,1]
print(findMaxConsecutiveOnes(arr))  # Output: 3

