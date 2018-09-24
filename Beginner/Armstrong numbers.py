m=int(input("Enter the starting value:"))
n=int(input("Enter the ending value:"))
for i in range(m,n):
    t=i
    s=0
    while(t>0):
        r=t%10
        s=s+(r*r*r)
        t=t//10
    if(i==s):
        print(i)
