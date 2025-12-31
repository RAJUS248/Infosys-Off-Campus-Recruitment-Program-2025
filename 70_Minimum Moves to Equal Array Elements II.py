def minMoves2(nums):

    nums.sort()

    n = len(nums)

    if n % 2 == 0:
        mid = nums[n // 2]

    else:
        mid = nums[(n+1) // 2]


    move = 0

    for num in nums:

        move += abs(num - mid)

    return move

nums = [1, 10, 2, 9]
print(minMoves2(nums))
