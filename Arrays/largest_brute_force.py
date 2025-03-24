myList1 = [2,4,5,32,6,255,5,42]
n = len(myList1)
# inplace sorting
for i in range(0, n):
    for j in range(i+1, n):
        if myList1[i] > myList1[j]:
            temp = myList1[i]
            myList1[i] = myList1[j]
            myList1[j] = temp
print(myList1)
# Find the largest element from the sorted list
print(myList1[-1])
# Time Complexity - O(n^2) (nestd Two loops)

