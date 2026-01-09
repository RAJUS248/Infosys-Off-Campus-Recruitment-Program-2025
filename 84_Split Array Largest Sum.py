def splitArray(nums, k):

    def can_split(max_cap):

        split = 1
        cur_sum = 0

        for num in nums:
            
            if cur_sum + num > max_cap:

                split += 1
                cur_sum = num

            else:
                cur_sum += num

        return split <= k
    
    low = max(nums)
    high = sum(nums)

    while low < high:

        mid = (low + high) // 2

        if can_split(mid):

            high = mid

        else:
            low = mid + 1

    return low


nums = [7,2,5,10,8]
k = 2

print(splitArray(nums,k))