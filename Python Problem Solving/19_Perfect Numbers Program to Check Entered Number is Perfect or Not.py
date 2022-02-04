# Perfect Numbers:  a number is called perfect number if the sum of all divisors of the number excluding that number 
# Example:  6 = 1+ 2 + 3   ---> 6 is perfect number
# 4 != 1 + 2   ---> 4 is not a perfect number

n = int(input("Type the number: "))
sum = 0
for i in range(1,n):
    if n%i ==0:
        sum = i + sum
    else:
        None

if sum == n:
    print(f"the number {n} is PERFECT number")
else:
    print(f"the number {n} is NOT PERFECT number")
    

        
