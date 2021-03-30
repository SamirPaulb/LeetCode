'''
   *
  * *
 *   *
*******
'''
n = int(input("Type how many rows you want:   "))
for row in range(1,n+1):
    for col in range(1,2*n):
        if row ==n or col - row == n-1 or col + row == n+1 :
            print("*", end="")
        else:
            print(end=" ")
    print()

