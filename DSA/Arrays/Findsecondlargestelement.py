# Example:
# array length = 3
# input array={2,2,2}
# return -1 as only (2) same value exist
# if input array ={2,1,2}
# return 1
#--------------------------
#Brute Force
arr=[2,3,1]
arr=sorted(arr)# T.C o(n log n) , S.C o(n)
largest=arr[len(arr)-1] # o(1)
slargest=0 # o(1)
for i in range(len(arr)-2,-1,-1): # T.C o(n-1)
    if(arr[i]!=largest):
        slargest=arr[i]
        break
print(slargest)
# T.C : o(n log n) + o (n-1) = o(n log n)
# S.C : o(n) + o(1) + 0(1) = o(n)
#---------------------------


#----------------------------
#Better
ar=[2,3,1]
largest=ar[0] # S.C : o(1)
for i in range(1,len(ar)): # T.C : o(n-1)
    if(ar[i]>largest): # T.C : O(n-1)
        largest=ar[i] # S.C : o(1)

slargest=-1 # S.C : o(1)
for i in range(len(ar)): # T.C : o(n)
    if(ar[i]>slargest and ar[i]!=largest):
        slargest=ar[i]

print(slargest)

# T.C : O(n)
# S.C : O(1)

#----------------------------
#Optimal
ar = [2, 3, 1]

largest = float('-inf')   # smallest possible value
slargest = float('-inf')

for num in ar:  # O(n)
    if num > largest:
        slargest = largest   # old largest becomes second largest
        largest = num
    elif num > slargest and num != largest:
        slargest = num

print("Largest:", largest)     # 3
print("Second Largest:", slargest)  # 2

# 🔹 Complexity

# Time Complexity:

# Single loop → O(n) ✅

# Space Complexity:

# Only a few variables → O(1) ✅












# Your code:

# ```python
# arr = [2, 3, 1]
# arr = sorted(arr)
# print(arr[1])
# ```

# ---

# ### Step 1: What’s happening

# 1. You define `arr = [2, 3, 1]`
# 2. `sorted(arr)` creates a **new sorted list** → `[1, 2, 3]`

#    * This does **not sort in place**, it returns a new list.
# 3. `arr` is reassigned to `[1, 2, 3]`
# 4. `arr[1]` → `2` gets printed.

# ---

# ### Step 2: Time Complexity

# * `sorted()` in Python uses **Timsort** (hybrid of merge sort + insertion sort).
# * **Best case:** `O(n)` (when list is already sorted).
# * **Average case:** `O(n log n)`
# * **Worst case:** `O(n log n)`

# Here `n = len(arr)`

# So, for this case with 3 elements → `O(3 log 3)` ≈ constant.
# But generally: **`O(n log n)`**

# ---

# ### Step 3: Space Complexity

# * `sorted()` creates a **new list** (unlike `.sort()` which sorts in-place).
# * Timsort needs **O(n)** additional space for merging.

# So:

# * **Auxiliary space:** `O(n)`
# * **Total space:** `O(n)`

# ---

# ✅ **Final Answer**

# * **Time Complexity:** `O(n log n)` (average/worst)
# * **Space Complexity:** `O(n)` (new list + Timsort’s buffer)

# ---

# Do you also want me to compare with using `arr.sort()` (in-place sort), so you clearly see the difference in time/space?

#Linear (O(n))

#“Linear” means the time or space grows in direct proportion to n (the input size).

# Good question 👌 Let’s clear this confusion.

# ---

# ### **1. Auxiliary Space**

# * This is the **extra memory** an algorithm needs **apart from the input data itself**.
# * Think of it as the *“temporary workspace”* the algorithm uses.

# For example:

# * Merge Sort → needs extra arrays to merge → **O(n) auxiliary space**.
# * Quick Sort → uses recursion stack → **O(log n) auxiliary space** (average).

# ---

# ### **2. Total Space**

# * This is the **overall memory** used = Input storage + Auxiliary space.

# So:

# ```
# Total Space = Input Space + Auxiliary Space
# ```

# ---

# ### **Your Code:**

# ```python
# arr = [2, 3, 1]
# arr = sorted(arr)
# ```

# * Input space: to store `arr` → **O(n)**
# * Auxiliary space (Timsort’s working + new sorted list) → **O(n)**
# * Total = **O(n) + O(n) = O(n)**

# ---

# ✅ **Summary**

# * **Auxiliary space** → extra workspace beyond input.
# * **Total space** → input + auxiliary.

