# create a function to find smallest value in array
def findSmallest(arr):
    # variable to store smallest value
    smallest = arr[0]

    # variable to store index of smallest value
    smallest_index = 0

    # for loop to go through each item
    for i in range(1, len(arr)):
        # compare value at index i to smallest
        if arr[i] < smallest:
            # if index value at i is smaller, index value becomes smallest
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# create function to select sort
def selectionSort(arr):
    # create empty array
    newArr = []

    # for loop to go through each element in array
    for i in range(len(arr)):
        # use smallest function to find smallest element in array
        smallest = findSmallest(arr)
        # remove smallest element from array
        newArr.append(arr.pop(smallest))
    
    # return new array
    return newArr

array = [100, 5, 72, 41, 80, 1, 99, 36, 27, 78]

print(selectionSort(array)) # [1, 5, 27, 36, 41, 72, 78, 80, 99, 100]