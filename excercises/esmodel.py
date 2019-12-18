file1 = open("model8.pdb", "r")
def CA(file,m):
	ca = []
	for line in file: 
		line.rstrip()
		cord = []
		if "CA" in line: 
			line = line.split()
			for i in range(m,m+3):
				cord.append(line[i])
			ca.append(cord)
	return(ca)
x = CA(file1,6)
print(x)
file1.close()
file2 = open("MODEL2","r")
y = CA(file2,5)
print(y)
file2.close()

from math import *
def rmsd(x,y):
	t = 0 
	for i in range(len(x)):
		z=0 
		for j in range(3):
			p = (float(x[i][j])-float(y[i][j]))**2
			z = z +p 
		t = t + z
	square =  sqrt(t/len(x))
	return(square)
print(rmsd(x,y))