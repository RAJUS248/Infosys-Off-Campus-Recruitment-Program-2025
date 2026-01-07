def eraseOverlapIntervals(intervals):

    if not intervals:
        return 0
    
    intervals.sort(key=lambda x:x[1])

    end = intervals[0][1]
    remv = 0

    for i in range(1,len(intervals)):
        cur_start = intervals[i][0]
        cur_end = intervals[i][1]

        if cur_start < end:

            remv += 1

        else:
            end = cur_end

    return remv


intervals = [[1,2],[2,3],[3,4],[1,3]]
print(eraseOverlapIntervals(intervals))



def eraseOverlapIntervals_v2(intervals):

    if not intervals:
        return 0
    
    intervals.sort(key=lambda x:x[1])

    end = float('-inf')
    remv = 0

    for x , y in intervals:

        if x < end:

            remv += 1

        else:
            end = y

    return remv


intervals = [[1,2],[2,3],[3,4],[1,3]]
print(eraseOverlapIntervals_v2(intervals))