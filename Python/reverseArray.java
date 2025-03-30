def reverseArray(arr):
    left, right =0, len(arr)-1
    while left<right:
        # Swap elements
        arr[left], arr[right] = arr[right], arr[left]
        # Move pointers
        left += 1
        right -= 1

arr = [1,2,3,4,5]
print("Original Array: ")
print(arr)

reverseArray(arr)

print("Reversed Array: ")
print(arr)
