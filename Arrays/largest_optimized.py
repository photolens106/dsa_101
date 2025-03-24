myList1 = [2,4,5,32,6,255,5,42]
maximum = myList1[0]
for element in myList1:
    if element>maximum:
        maximum = element
print(maximum)

# O(n)