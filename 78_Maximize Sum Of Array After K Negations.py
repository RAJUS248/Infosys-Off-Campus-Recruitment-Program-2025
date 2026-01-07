def largestSumAfterKNegations(nums, k):

    nums.sort()
    i = 0
    while k > 0 and i < len(nums):

        
        if nums[i] < 0:
            nums[i] = -nums[i]
            k -= 1
            i += 1

        else:

            break

    if k % 2 == 1:
        nums.sort()
        nums[0] = -nums[0]

    return sum(nums)

nums = [3,-1,0,2]
k = 3
print(largestSumAfterKNegations(nums,k))