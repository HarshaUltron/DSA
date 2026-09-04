n = 6
arr = [13,46,24,52,20,9]
print(arr)

class Solution:
    def SelectionSort(self,n,arr):
        
        for i in range(n):
         # Assume current index has the minimum value
         min_index = i

         # Find the smallest element in remaining array
         for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

         # Swap the found minimum element with current element
         arr[i], arr[min_index] = arr[min_index], arr[i]

        return arr

df=Solution()
n = 6
arr = [13,46,24,52,20,9]
print(arr)
print(df.SelectionSort(n,arr))

"""
Time Complexity Analysis
Time Complexity : O(n2) , even for sorted array it will check every element in every pass
Space Complexity : O(1) , how big the size of array, we use only constant space to run this algorithm

"""