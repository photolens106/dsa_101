myList1 = [1,2,4,7,6,7,5]
# 1st pass finding the largest
largest = myList1[0]
for element in myList1:
    if element>largest:
        largest = element
print(largest)
# 2nd pass finding the second largest
secondLargest = -1
for element in myList1:
    if element>secondLargest and element!=largest:
        secondLargest = element
print(secondLargest)

"""
Time Complexity = 

1st pass = O(n)
2nd pass = O(n)
Total = O(2n)
"""
