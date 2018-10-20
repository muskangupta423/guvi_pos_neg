n=int(input())
l=list(map(str,input().split()))
m=l[0]
m=int(m)
for i in range(len(l)):
	if(l[i].isalpha()):
		print('Invalid Input')
		exit()		
	else:
		if(int(l[i])>m):
			m=int(l[i])
print(m)				
