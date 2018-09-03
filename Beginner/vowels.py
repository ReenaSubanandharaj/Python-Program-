z=['a','e','i','o','u']
print("enter the value")
x=input()
if(x.isalpha()):
    if(x in z):
        print("vowel")
    else:
	print("consonant")
else:
	print("invalid")
