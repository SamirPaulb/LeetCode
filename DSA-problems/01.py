n = int(input("Wrrite a number here: \n"))

total_sum = 0
for i in range(n+1):
    total_sum = total_sum + i

avg = total_sum/n
print(f" Average of {n} numbers is {avg}")

