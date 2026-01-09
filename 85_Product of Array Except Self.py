def productExceptSelf(nums):

    left_product = [1]
    pro = 1
    for i in range(1,len(nums)):
        pro *= nums[i-1]

        left_product.append(pro)

    right_product = [1]

    pror = 1
    for i in range(len(nums)-1,0,-1):
        pror *= nums[i]
        right_product.append(pror)

    right_product.reverse()

    ans = []
    for i in range(len(nums)):
        ans.append(left_product[i] * right_product[i])


    return ans
nums = [1,2,3,4]
print(productExceptSelf(nums))


def productExceptSelf_v2(nums):

    n =len(nums)
    answer = [1] * n

    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n-1,-1,-1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer

nums = [1,2,3,4]
print(productExceptSelf_v2(nums))
