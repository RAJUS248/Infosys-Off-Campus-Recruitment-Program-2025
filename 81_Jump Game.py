def canJump(nums):

    max_reach = 0

    for i in range(len(nums)):

        if i > max_reach:
            return False
        
        max_reach = max(max_reach, i + nums[i])

    return True

nums = [2,1,0,2,2,0,3]
print(canJump(nums))