f=open("test1.txt",'r')
lines=f.readlines()
for line in lines:
	print(line),
f.close()
