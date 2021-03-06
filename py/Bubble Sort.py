"""
Bubble Sort

Iterate through list and compare each pair to determine which is larger

Switch each pair which shows the next index containing a value less than the current value

"""

array = [5, 9, 22, 0, 64, 203, 44, 56, 2]

"Takes in array as input and orders it by increasing value"

def bubble_sort(arr):
    length = len(array)

    'Iterate through entire array'
    for i in range(length):

        'Check each value vs the value in front of it'
        for j in range(length - i - 1):

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return arr


print(bubble_sort(array))
