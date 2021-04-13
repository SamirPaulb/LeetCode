n = int(input("Enter upto which digit you want to find Angstrom number:  "))

for i in range(1,n+1):
    l = len(str(i))
    result = 0
    a = str(i)
    for j in range(l):
        result = result + int(a[j])**l
    if result == i:
        print(i)
    



