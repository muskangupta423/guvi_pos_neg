import math
N1=input("enter 1st number")
N2=input("enter 2nd number")
l=[]
l.append(2)
if(N1.isdigit() and N2.isdigit()):
	for i in range(int(N1),int(N2)):
		if(2**i%i==2):
			l.append(i)
	if(int(N1)<2):
		print(l)
	else:
		print(l[1::])
else:
	print("Invalid")
	
