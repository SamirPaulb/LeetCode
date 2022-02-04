'''
   *
  * *
 *   *
* * * *
'''

n = int(input("Type no. of rows: "))
for row in range(1,n+1):
    for col in range(1,2*n):
        if row == n :
            if col%2 !=0:
                print("*",end="")
            else:
                print(end=" ")
        elif row + col == n+1 or col -row == n-1 :
            print("*",end="")
        else:
            print(end=" ")
    print()
