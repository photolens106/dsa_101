arr = [1,2,4,7,6,7,5]

largest = arr[0]
"""
In this optimized problem you can assume all elements are positive 
then you can give the secondLargest = -1
but Here we will be also giving priority to negative numbers too.
"""
secondLargest = float('-inf')   # Smallest number
n = len(arr)
for i in range(1, n):
    if (arr[i] > largest):
        secondLargest = largest
        largest = arr[i]
    elif (arr[i]<largest and arr[i]>secondLargest):
        secondLargest = arr[i]
print(secondLargest)


# Time Complexity - O(n)

