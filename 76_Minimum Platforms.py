def minPlatform(arr, dep):

    n = len(arr)
    arr.sort()
    dep.sort()

    platform_need = 0
    max_platform = 0

    i = 0
    j = 0

    while i < n and j < n:

        if arr[i] <= dep[j]:
            platform_need += 1 
            i += 1

            if platform_need > max_platform:
                max_platform = platform_need

        else:
            platform_need -= 1
            j += 1

    return max_platform


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]

print(minPlatform(arr,dep))