N,A,D=input().split()
if(N.isdigit() and A.isdigit() and D.isdigit() and (int(N) and int(A) and int(D))<=100000 and (int(N) and int(A) and int(D))>0):
	N=int(N)
	A=int(A)
	D=int(D)
	s=(N*(2*A+(N-1)*D))//2
	print(s)
else:
	print('Invalid Input')