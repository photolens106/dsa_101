# Check if the array is sorted in non-descending order
def check_if_array_sorted(arr):
    for i in range(1, len(arr)):
        if not (arr[i]>=arr[i-1]):
            return False
    return True

arr1 = [1,2,1,3,4]
if (check_if_array_sorted(arr1)):
    print("Array is Sorted")
else:
    print("Array is not sorted")