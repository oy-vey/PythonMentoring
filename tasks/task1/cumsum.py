# Function that takes a list of numbers and returns it cummulative sum
def cumsum(numbers):
    temp = 0
    cumsums = []
    for v in numbers:
        temp = temp + v
        cumsums.append(temp)

    print ('Values: ', numbers)
    print ('Sums:   ', cumsums)

cumsum([2,3,6])