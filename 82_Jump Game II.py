def jump(nums):

    jumps = 0
    farthest = 0
    current = 0

    for i in range(len(nums)-1):

        farthest = max(farthest, i + nums[i])

        if i == current :
            current = farthest
            jumps += 1
    
    return jumps

nums = [2,3,1,1,4]
print(jump(nums))