# Find the second largest element from the array 

# Brute Force method 
myList1 = [1,2,4,7,6,7,5]
n = len(myList1)
# inplace sorting
for i in range(0, n):
    for j in range(i+1, n):
        if myList1[i] > myList1[j]:
            temp = myList1[i]
            myList1[i] = myList1[j]
            myList1[j] = temp
largest = myList1[-1]
elem = n-2
while (elem>=0):
    if (myList1[elem]!=largest):
        second = myList1[elem]
        break
    elem-=1
print(second)


"""
Sorting takes O(nlogn)
Traversing - O(n)
Time Complexity - nlogn + n
"""

