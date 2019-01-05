********************************************************************************
# Quicksort Big O
# Quick sort average case is O(n log n)
    # each level takes O(n) but splitting the data is O(log n)
    # O(n) * O(log n) = O(n log n)
# Worse case is O(log n2)
    # if pivot is smallest value, each level is O(n) and splitting the data is O(n)
    # O(n) * O(n) = O(n2)
********************************************************************************


# array
array = [100, 5, 72, 41, 80, 1, 99, 36, 27, 78]

# quicksort function
def quicksort(array):
    # if length of array is 0 or 1, return the array
    if len(array) < 2:
        return array
    else:
        # create a base case
        pivot = array[0]
        # use list comprehension to build list of elements less than pivot
        less = [i for i in array[1:] if i <= pivot]
        # use list comprehension to build list of elements greater than pivot
        greater = [i for i in array[1:] if i > pivot]
        # call quicksort function again on less and greater lists
        return quicksort(less) + [pivot] + quicksort(greater)

# run recursive function on array
print(quicksort(array)) # [1, 5, 27, 36, 41, 72, 78, 80, 99, 100]

