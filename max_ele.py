n=int(input())
lst=list(map(str,input().split()))
m=l[0]
for i in range(len(lst)):
	if(lst[i].isalpha()):
		print('Invalid Input')
		exit()		
	else:
		if(lst[i]>m):
			m=lst[i]
print(m)
