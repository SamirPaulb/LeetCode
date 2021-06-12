def BinarySearch(l,key):
    low = 0
    high = len(l)-1
    mid = (low+high)//2
    found = False
    while low<=high and not found:
        mid = (low+high)//2
        if key == l[mid] :
            mid = mid -1
            found = True
        elif key < l[mid]:
            high = mid -1
        elif key > l[mid]:
            low = mid +1
    if found ==True:
        print("The key is found!")
        print(mid)
    else:
        print("The key is not found.")

l = [1,2,4,5,97,97,97,97,97,324,5464,5555555]
#key = int(input("enter a value within the list:  "))
BinarySearch(l,97)