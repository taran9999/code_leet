def solution(target, position, speed):
    car_info = list(zip(position, speed))
    car_info.sort() # sorted by position

    stack = []
    for i in range(len(car_info)):
        time = (target - car_info[i][0]) / car_info[i][1]
        while len(stack) > 0 and time >= stack[-1][1]:
            # this car is ahead and will take more time than the one on the stack
            # note cars can't pass each other, so these two are forced to form a fleet
            # we pop every car that forms a fleet with the one we are pushing so only one car from each fleet
            # is on the stack
            stack.pop()
        stack.append((i, time))

    return len(stack)