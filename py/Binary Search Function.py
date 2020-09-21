#Implement a Binary Search Function


#An algorithm for searching through an ordered list of numerical objects for a given value
import time

def binary_search(value):

    #Ordered List
    list = [0,22,30,56,546,2102, 58956]
    beginning = 0
    end = len(list) - 1

    """
    Check whether item in the center of the list is greater than or
    less than value we are seeking
    
    """
    mid = int((beginning + end)/2)

    while end >= beginning:
        print(mid)
        time.sleep(1)
        #Return the position if value matches our goal
        if list[mid] == value:
            return "At Position: " + str(mid)

        #Eliminate the half of the list we know our value is not in
        elif list[mid] >= value:
            end = mid - 1
            mid = int((beginning + end)/2)
        elif list[mid] <= value:
            beginning = mid + 1
            mid = int((beginning + end)/2)
    return "Not in list"

print(binary_search(2102))
print(binary_search(25))
print(binary_search(0))
print(binary_search(56))
print(binary_search(15563561))


