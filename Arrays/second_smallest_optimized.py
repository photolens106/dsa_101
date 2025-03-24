arr = [1,2,4,7,6,7,5]

smallest = arr[0]
"""
In this optimized problem you can assume all elements are positive 
then you can give the secondLargest = -1
but Here we will be also giving priority to negative numbers too.
"""
secondSmallest = float('inf')   # Largest number
n = len(arr)
for i in range(1, n):
    if (arr[i] < smallest):
        secondSmallest = smallest
        smallest = arr[i]
    elif (arr[i]!=smallest and arr[i]<secondSmallest):
        secondSmallest = arr[i]
print(secondSmallest)


# Time Complexity - O(n)

