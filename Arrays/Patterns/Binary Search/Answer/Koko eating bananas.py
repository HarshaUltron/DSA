class Solution:
    def kokoEat(self, arr, k):
        left = 1
        right = max(arr)

        while left <= right:
            mid = left + (right - left) // 2

            hours = 0

            for pile in arr:
                hours += (pile + mid - 1) // mid

            if hours <= k:
                # This speed works, try a smaller speed
                right = mid - 1
            else:
                # Too slow, increase speed
                left = mid + 1

        return left




#     If you mean this:

# ```python
# (pile + mid - 1) // mid
# ```

# the `+ mid - 1` is a trick to calculate **ceiling division** using integer division.

# We need:

# ```text
# ceil(pile / mid)
# ```

# because if Koko eats `mid` bananas/hour, a partially completed final hour still counts as a **full hour**.

# ### Example: 10 bananas, speed 4

# Normal integer division:

# ```python
# 10 // 4
# ```

# gives:

# ```text
# 2
# ```

# But Koko actually needs **3 hours**:

# ```text
# Hour 1 → 4
# Hour 2 → 4
# Hour 3 → 2
# ```

# So we need `ceil(10/4) = 3`.

# The trick:

# ```python
# (10 + 4 - 1) // 4
# ```

# becomes:

# ```text
# 13 // 4 = 3
# ```

# ### Why does it work?

# For any positive integers:

# ```text
# ceil(a / b) = (a + b - 1) // b
# ```

# Examples:

# ```text
# 10 / 4 → ceil = 3
# (10 + 4 - 1) // 4 = 3

# 7 / 4 → ceil = 2
# (7 + 4 - 1) // 4 = 2

# 8 / 4 → ceil = 2
# (8 + 4 - 1) // 4 = 2
# ```

# Notice the last one:

# ```text
# 8 / 4 = exactly 2
# ```

# and the formula still gives `2`.

# ### For Koko

# So:

# ```python
# hours += (pile + mid - 1) // mid
# ```

# simply means:

# > **"How many whole hours does Koko need to finish this pile at speed `mid`?"**

# And because she can only eat from one pile per hour, we calculate this **separately for every pile** and add them together.
