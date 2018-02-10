import pickle
f=open("text2.txt",'rb')
for i in range(1,11):
	data = pickle.load(f)
	print(data)
f.close()
