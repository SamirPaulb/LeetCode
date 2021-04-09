s = input("Enter a String to check Pailindrome:   ")
rev_s = s[::-1]
if s == rev_s:
    print(f"{s} is a Pailindrome")
else:
    print("Entered String is NOT a Pailindrome")






'''

s = input("Enter a String to check Pailindrome:   ")
rev_s = s[::-1]

if len(s)%2 ==0:
    a = []
    for i in range(int(len(s)/2) ):
        if s[i] == rev_s[i]:
            a.append(1)
    if len(a) == int(len(s)/2):
        print("Entered String is a Pailindrome")
    else:
        print("Entered String is NOT a Pailindrome")

        

elif len(s)%2 !=0:
    b = []
    for i in range(int(len(s)/2)):
        if s[i] == rev_s[i]:
            b.append(1)
    if len(b) == int(len(s)/2):
        print("Entered String is a Pailindrome")
    else:
        print("Entered String is NOT a Pailindrome")

'''



