n=int(input("Enter the number:"))
f=0
for i in range(2,n-1):
  if(n%i==0):
    f=1
if(f==1):
  print(n,"is not a prime number")
else:
  print(n," is a prime number")
