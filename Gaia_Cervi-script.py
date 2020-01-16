import input_data

alignments = input_data.alignments


blosum62 = open("./blosum62.txt","r")
dblosum62= {}
i = 0
for line in blosum62: 
	if i == 0:
		L = line.split()
		i = 1
	else:
		line1 = line.split()
		AA = line1[0]
		scores = line1[1:]
		for j in range(len(L)):
			couple = L[j] + AA
			value = scores[j]
			dblosum62[couple]=value
print(dblosum62)

pam250 = open("./PAM250.txt","r")
dpam250 = {}
i = 0
for line in pam250: 
	if i == 0:
		L = line.split()
		i = 1
	else:
		line1 = line.split()
		AA = line1[0]
		scores = line1[1:]
		for j in range(len(L)):
			couple = L[j] + AA
			value = scores[j]
			dpam250[couple]=value
print(dpam250)

def alignment_score(l):
	for j in l: 
		PAM_score = 0 
		BLOSUM_score = 0
		for i in range(len(j[0])):
			dict_key = j[0][i]+j[1][i]
			if "-" in dict_key:
				PAM_score -= -2
				BLOSUM_score -= -2
			else:
				PAM_score = PAM_score + int(dpam250[dict_key])
				BLOSUM_score += int(dblosum62[dict_key])
		print(PAM_score, BLOSUM_score, j)

print(alignment_score(alignments))