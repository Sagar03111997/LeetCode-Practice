def search(array, x):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return low
        

print(search([1,3,5,6], 5))