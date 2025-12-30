def eliminateMaximum(dist: list[int], speed: list[int]) -> int:

    arival_time = []

    for i in range(len(dist)):

        time =  dist[i] / speed[i]

        arival_time.append(time)

    arival_time.sort()

    for i in range(len(arival_time)):

        if arival_time[i] <= i:
            return i
        
    return len(dist)

dist = [3,2,4]
speed = [5,3,2]

print(eliminateMaximum(dist,speed))