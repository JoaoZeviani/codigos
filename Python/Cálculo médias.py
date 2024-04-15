notas_ac = [float(x) for x in input().split()]
notas_lo = [float(x) for x in input().split()]
peso_lo = [float(x) for x in input().split()]
notas_la = [float(x) for x in input().split()]
peso_la = [float(x) for x in input().split()]
notas_p = [float(x) for x in input().split()]
freq = float(input())

exame = 1000

Mac = sum(notas_ac)/len(notas_ac)

lo = []
for i in range(len(notas_lo)):
	a = notas_lo[i]*peso_lo[i]	
	lo.append(a)
la = []
for i in range(len(notas_la)):
	a = notas_la[i]*peso_la[i]	
	la.append(a)

Ml = (sum(lo)+sum(la))/sum(peso_lo)


Mp = notas_p[0]*2/5+notas_p[1]*3/5

if Mp >= 2.5 and Ml >= 2.5  and (Mp < 5 or Ml < 5):
	exame = float(input())

print("Media das atividades conceituais: {:.1f}".format(Mac))
print("Media das tarefas de laboratorio: {:.1f}".format(Ml))
print("Media das provas: {:.1f}".format(Mp))
if exame != 1000: print("Nota no exame: {:.1f}".format(exame))

if freq >= 75:
	if Mp >= 5 and Ml >= 5:
		Melem = 0.6 * Mp + 0.3 * Ml + 0.1 * Mac
		Mfinal = max(5, Melem)
	
	elif Mp >= 2.5 and Ml >= 2.5:
		Mfinal = (min(Mp, Ml) + exame)/2.
	
	else: Mfinal = min(Mp, Ml)
	
	if Mfinal >= 5:
		print("Aprovado(a) por nota e frequencia.")
	else: print("Reprovado(a) por nota.")

else:
	print("Reprovado(a) por frequencia.")
	Mfinal = min(Mp, Ml)


Mfinal = min(10,Mfinal)

print("Media final: {:.1f}".format(Mfinal)) 




