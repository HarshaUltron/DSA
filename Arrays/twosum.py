def twoSum(arr, k):
    seen = {}  # stores number → index
    for i, num in enumerate(arr):
        complement = k - num
        if complement in seen:   # found a match
            return [seen[complement], i]
        seen[num] = i   # store current number
    return []
