n=int(input("Enter the number:"))
t=n
rev=0
while(n>0):
    r=n%10
    rev=(rev*10)+r
    n=n//10
if(t==rev):
    print(n,"is palindrome")
else:
    print(n,"is not a palindrome")
