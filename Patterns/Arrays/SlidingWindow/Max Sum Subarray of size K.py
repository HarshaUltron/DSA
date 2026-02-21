class Solution:
    def maxSubarraySum(self, arr, k):
        n = len(arr)
        if k > n:
            return -1

        window_sum = sum(arr[:k])
        max_sum = window_sum

        for i in range(k, n):
            window_sum += arr[i] - arr[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum

df=Solution()
print(df.maxSubarraySum([100, 200, 300, 400], k = 2))