'''
		Resolvido por: Ruan Ferreira
		Data: 29/07/19
		**Maratona de Programação da SBC – 2017**
		Questão: Acordes Intergaláticos
'''
##recebe a fatia de uma lista e retorna o elemento mais comum
def most_common(L):
	count = 0
	higher = 0
	for i in L:
		if (L.count(i) > count):
			higher = i
			count = L.count(i)
		elif (L.count(i) == count):
			 if i > higher:
			 	higher = i
			 	count = L.count(i)
	print(higher)
	return higher

x = input().split(' ')
N = []
Q = []

for y in range(int(x[0])):
	N.append(1)

for y in range(int(x[1])):
	note = input().split(' ')
	Q.append([int(note[0]), int(note[1])])

for note in Q:
	x = note[0]
	y = note[1]
	F = most_common(N[x:y+1])
	while x <= y:
		N[x] += F
		if N[x] >= 9:
			N[x] -= 9
		x += 1
print(N)
