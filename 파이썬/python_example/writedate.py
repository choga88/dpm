with open("test1.txt",'w') as f:
  for i in range (1,11):
     data ="%s line.\n" %i
     f.write(data)
