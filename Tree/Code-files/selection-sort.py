## Time Complexity : O(n^2)
## Function Definition
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        ## to store the index of the minimum element
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        ## swap of the element at i and min_idx
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr
## Driver code
arr = [50, 38, 75, 29, 11, 17, 20, 37]
## Function calling
result = selectionSort(arr)
print("Selection Sort of the given array elements is:", result)