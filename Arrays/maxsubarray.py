# arr = [5,4,-1,7,8]
# n = len(arr)

# max_sum = float('-inf')
# subarr = []

# for start in range(n):
#     subarray = []
#     current_sum = 0
#     for end in range(start, n):
#         current_sum += arr[end]
#         subarray.append(arr[end])
#         if current_sum > max_sum:
#             max_sum = current_sum
#             subarr = subarray[:]   # <-- make a copy
# print("Maximum subarray:", subarr)
# print("Maximum sum:", max_sum)

# T.C : O(n^2)
# S.C : O(1)

# Kaden's algorithm


arr = [-2,1,-3,4,-1,2,1,-5,4]

max_sum = float('-inf')
current_sum = 0

start = 0
end = 0
temp_start = 0

for i in range(len(arr)):
    # Decide whether to continue or start fresh
    if current_sum + arr[i] < arr[i]:
        current_sum = arr[i]
        #temp_start = i   # new subarray starts here
    else:
        current_sum += arr[i]

    # Update max if needed
    if current_sum > max_sum:
        max_sum = current_sum
        # start = temp_start
        # end = i

#print("Maximum Subarray:", arr[start:end+1])
print("Maximum Sum:", max_sum)
