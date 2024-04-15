n = int(input())

nj = n*(n-1)-1

times = []
pontos = []
vitorias = []
gols_marcados = []
gols_sofridos = []
jogos = []

for i in range(n):
	pontos.append(0)
	vitorias.append(0)
	gols_marcados.append(0)
	gols_sofridos.append(0)
	jogos.append(0)

inf = []

for i in range(nj):
	j = [(x) for x in input().split()]
	inf.append(j)

for i in range(nj):
	if inf[i][0] not in times:
		times.append(inf[i][0])
	if inf[i][3] not in times:
		times.append(inf[i][3])

for i in range(nj):
	time = times.index(inf[i][0])
	gols_marcados[time] += int(inf[i][1])
	gols_sofridos[time] += int(inf[i][4])
	jogos[time] += 1
	if int(inf[i][1]) > int(inf[i][4]):
		pontos[time] += 3
		vitorias[time] += 1
	elif int(inf[i][1]) == int(inf[i][4]):
		pontos[time] += 1
	time = times.index(inf[i][3])
	gols_marcados[time] += int(inf[i][4])
	gols_sofridos[time] += int(inf[i][1])
	jogos[time] += 1
	if int(inf[i][4]) > int(inf[i][1]):
		pontos[time] += 3
		vitorias[time] += 1
	elif int(inf[i][4]) == int(inf[i][1]):
		pontos[time] += 1

i_time1 = jogos.index((n-3/2)*2)
i_time2 = jogos.index((n-3/2)*2,i_time1+1)

time1 = str(times[i_time1])
time2 = str(times[i_time2])

jogos_casa = 0
for i in range(nj):
    if time1 == inf[i][0]:
        jogos_casa+=1
if jogos_casa == n-2:
    time1, time2 = time2, time1
    

jogo_faltante = []
jogo_faltante.append(time2)
jogo_faltante.append('10')
jogo_faltante.append('x')
jogo_faltante.append(time1)
jogo_faltante.append('0')

time = times.index(jogo_faltante[0])
gols_marcados[time] += int(jogo_faltante[1])
gols_sofridos[time] += int(jogo_faltante[4])
jogos[time] += 1
if int(jogo_faltante[1]) > int(jogo_faltante[4]):
	pontos[time] += 3
	vitorias[time] += 1
elif int(inf[1]) == int(jogo_faltante[4]):
	pontos[time] += 1
time = times.index(jogo_faltante[3])
gols_marcados[time] += int(jogo_faltante[4])
gols_sofridos[time] += int(jogo_faltante[1])
jogos[time] += 1
if int(jogo_faltante[4]) > int(jogo_faltante[1]):
	pontos[time] += 3
	vitorias[time] += 1
elif int(jogo_faltante[4]) == int(jogo_faltante[1]):
	pontos[time] += 1

saldo = [gols_marcados[i] - gols_sofridos[i] for i in range(len(gols_marcados))]


matriz_colocacao = []
for i in range(n):
	a = []
	for i in range(4):
		a.append(0)
	matriz_colocacao.append(a)
for i in range(n):
	matriz_colocacao[i].append(i)

i_times_selecionados = [pontos.index(max(pontos))]

for i in range(pontos.count(max(pontos))-1):
		i_times_selecionados.append(pontos.index(max(pontos),max(0,i_times_selecionados[i-1]+1)))

for i in range(len(i_times_selecionados)):
	matriz_colocacao[i_times_selecionados[i]][0] = 1

i_times_selecionados = [vitorias.index(max(vitorias))]

for i in range(vitorias.count(max(vitorias))-1):
		i_times_selecionados.append(vitorias.index(max(vitorias),max(0,i_times_selecionados[i-1]+1)))

for i in range(len(i_times_selecionados)):
	matriz_colocacao[i_times_selecionados[i]][1] = 1

i_times_selecionados = [saldo.index(max(saldo))]

for i in range(saldo.count(max(saldo))-1):
		i_times_selecionados.append(saldo.index(max(saldo),max(0,i_times_selecionados[i-1]+1)))

for i in range(len(i_times_selecionados)):
	matriz_colocacao[i_times_selecionados[i]][2] = 1

i_times_selecionados = [gols_marcados.index(max(gols_marcados))]

for i in range(gols_marcados.count(max(gols_marcados))-1):
		i_times_selecionados.append(gols_marcados.index(max(gols_marcados),max(0,i_times_selecionados[i-1]+1)))

for i in range(len(i_times_selecionados)):
	matriz_colocacao[i_times_selecionados[i]][3] = 1

i_perdedores=[]
for j in range(4):
	for i in range(len(matriz_colocacao)):
		if len(i_perdedores) != n-1:
			if matriz_colocacao[i][j] == 0 and matriz_colocacao[i][4] not in i_perdedores:
				i_perdedores.append(matriz_colocacao[i][4])

i_campeao = list(set(list(range(n)))-set(i_perdedores))			

campeao = ['Campeao:']
campeoes = ['Campeoes:']
for i in range(len(i_campeao)):
    campeao.append(times[i_campeao[i]])
    campeoes.append(times[i_campeao[i]])

print(" ".join(jogo_faltante))

asd = list(zip(times,pontos,vitorias,saldo,gols_marcados))
asd.sort()
times,pontos,vitorias,saldo,gols_marcados = zip(*asd)

for i in range(len(times)):
	print(times[i],pontos[i],vitorias[i],saldo[i],gols_marcados[i])
    
if len(campeao) == 2:
    print(" ".join(campeao))
else:
    print(" ".join(campeoes))

if time2 in campeao:
	print('Meu time pode ser campeao!!!')