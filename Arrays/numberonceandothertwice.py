def singleNumber(nums):
    xor_sum = 0
    for num in nums:   # O(n)
        xor_sum ^= num
    return xor_sum
