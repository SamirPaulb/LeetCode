num = int(input("How many elements you want in the list:  "))
a = [int(input("Enter an element:  ")) for x in range(num) ]

# In increasing order

for i in range(len(a)):
    for j in range(i,len(a)):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
    
print(f"The sorted list in increasing order is:   {a}")


