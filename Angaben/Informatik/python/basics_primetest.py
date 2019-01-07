n = int(input())

prim = True	
for i in range(2, int(n/2)):
	if n % i == 0:
		prim = False
		break

if prim:
	print("Primzahl")
else:
	print("Keine Primzahl")
