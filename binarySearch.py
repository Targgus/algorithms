# sorted array
array = [2, 5, 8, 10, 15, 16, 22, 30, 31, 50, 52, 57, 61, 77, 80, 84, 89, 93, 97, 100]


def binarySearch(array, item):
    # set low and high starting positions
    low = 0
    high = len(array) - 1

    while low <= high:

        # find middle location of array
        mid = (low + high) // 2

        # determine middle element
        guess = array[mid]

        #compare guess (middle element) to item
        if guess == item:
            return mid
        # if guess is larger than item, high becomes middle element
        if guess > item:
            high = mid - 1
        # if guess is smaller than item, move low to middle element
        else:
            low = mid + 1
        
    return None


# call function on array
print(binarySearch(array, 8)) # 2

print(binarySearch(array, 7)) # None
