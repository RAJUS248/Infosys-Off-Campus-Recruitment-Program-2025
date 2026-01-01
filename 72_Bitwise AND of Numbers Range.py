def rangeBitwiseAnd(left, right):

    shift_count = 0
    while left != right:
            
        left = left >> 1
        right = right >> 1
        shift_count += 1

        if left == 0 or right == 0:
            return 0

    return left << shift_count

left = 1
right = 2147483647

print(rangeBitwiseAnd(left,right))