## Method definition
## Time Complexity : O(n^2)
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                ##swap of the elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

## Driver code
arr = [70, 20, 50, 30, 90, 5, 15]
result = bubbleSort(arr)
print("Array after applying bubble sort:", result)