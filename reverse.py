text= input()
if(text!=""):
	l= len(text)
	rev_str= ""
	while l>0:
	   rev_str+= text[l-1]
	   l=l-1
	print(rev_str)
else:
	print("Empty string")