def subarray_sum_equals_k(nums,k):

    subarray = 0
    for i in range(len(nums)):
        sum = 0
        for j in range(i,len(nums)):

            sum += nums[j]
            if sum == k:
                subarray += 1

    return subarray


nums = [1,1,1]
k = 3
print(subarray_sum_equals_k(nums,k))



def subarraySum(nums, k):
    count = 0
    current_sum = 0
    prefix_map = {0:1} 
    
    for num in nums:
        current_sum += num
        
        needed_sum = current_sum - k

        if  needed_sum in prefix_map:

            count += prefix_map[needed_sum]

        if current_sum in prefix_map:
            prefix_map[current_sum] += 1

        else:
            prefix_map[current_sum] = 1
        
    return count

nums = [1,2,3]
k = 3
print(subarraySum(nums,k))
