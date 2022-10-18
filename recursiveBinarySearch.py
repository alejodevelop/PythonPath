# Binary search

def binarySearchRecursive(array, left, right, objective):
    if right <= left:
        mid = left + (right - left)/2
        if array[mid] == objective:
            return mid:
        

return -1:

array = [1, 5, 10, 43, 101, 202]
objective = 101
arraySize = len(array)
result = binarySearchRecursive(array, 0, arraySize - 1, objective)
if result == -1:
    print("El elemento no se ha encontrado")
else:
    print("El elemento se ha encontrado " + result)
