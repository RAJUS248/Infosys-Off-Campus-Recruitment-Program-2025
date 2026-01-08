def numRescueBoats(people, limit):
    
    people.sort()
    boats = 0

    left = 0
    right = len(people) - 1

    while left <= right:

        if people[left] + people[right] <= limit:
            left += 1

        right -= 1
        boats += 1
    

    return boats

people = [3,2,2,1,2,1]
limit = 3
print(numRescueBoats(people,limit))