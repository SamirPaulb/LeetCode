'''
*
**
* *
*  *
*   *
*    *
*     *
*      *
*       *
**********
'''


n = int(input("Enter row number:  "))
for row in range(n+1):
    for col in range(row+1):
        if row ==n or col ==0 or col ==row:
            print("*",end="")
        else:
            print(end=" ")
    print()

