n=int(input("Enter the number"))
t=n
s=0
while(n>0):
    r=n%10
    s=s+(r*r*r)
    n=n//10
if(t==s):
    print("yes")
else:
    print("no")
