# Left rotate the array by one place (in the given array itself)
arr = [1,2,3,4,5]
print(arr)
temp = arr[0]
for i in range(1, len(arr)):
    arr[i-1] = arr[i]
arr[len(arr)-1] = temp
print(arr)

# Time Complexity - O(n)
# Space Complexity - 
    # algo - O(n)
    # extra space - O(1)
