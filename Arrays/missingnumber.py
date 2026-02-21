class Solution:
    def missingNumber(self, arr):
        n = len(arr)
        xor1 = 0
        xor2 = 0

        # XOR of all array elements
        for num in arr:
            xor1 ^= num

        # XOR of all numbers from 0..n
        for i in range(n+1):
            xor2 ^= i

        return xor1 ^ xor2
