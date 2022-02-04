'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

'''

n = int(input("type the number here: \n"))
num = 1
for row in range(1,n+1):
    for col in range(1,row+1):
        print(num, end=" ")
        num = num +1
    print()


