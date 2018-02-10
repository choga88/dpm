import pickle
f=open("text2.txt",'wb')
for i in range(1,11):
   data ="%s line.\n" %i
   pickle.dump(data,f)
f.close()
