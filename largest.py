a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
c=int(input("Enter 3rd number"))
if (a>b) and (a>c):
	print(a,"is largest")
elif b>c:
	print(b,"is largest")
else:
	print(c,"is largest")