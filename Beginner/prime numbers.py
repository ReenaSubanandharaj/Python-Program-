a=1
b=10
for i in range(a,b+1):
  if(i>1):
    for x in range(2,i):
      if(i%x==0):
        break
    else:
      print(i)
