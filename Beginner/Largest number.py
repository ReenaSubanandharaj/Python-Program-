a=int(input("Enter the first value:"))
b=int(input("Enter the second value:"))
c=int(input("Enter the third value:"))
if(a>b)and(a>c):
    print("The largest number is ",a) 
elif(b>a)and(b>c):
    print ("The largest number is ",b) 
else:
    print ("The largest number is ",c)
