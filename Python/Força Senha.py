n = int(input())
senhas = []
valor_senhas = [0]*n

for i in range(n):
    a = input()
    senhas.append(a)

senhas_aux=senhas[:]
    
for i in range(n):
    if len(senhas[i])>8:
        valor_senhas[i]+=(2*(len(senhas[i])-8))
    elif len(senhas[i])<8:
        valor_senhas[i]+=(-4*(8-len(senhas[i])))
        
for j in range(n):
    l = list(senhas[j])
    especial = 0
    letram = 0
    letraM = 0
    numero = 0
    for i in range(len(l)):
        if l[i]=='!' or l[i]=='@' or l[i]=='#' or l[i]=='"' or l[i]=='$' or l[i]=='%' or l[i]=='&' or l[i]=='*' or l[i]=='(' or l[i]==')' or l[i]=='[' or l[i]==']' or l[i]=='<' or l[i]=='>' or l[i]=='?' or l[i]=='.' or l[i]==',':
            especial+=1
    for i in range(len(l)):
        if l[i].isalpha():
            if l[i].islower():
                letram+=1
            else: letraM+=1
    for i in range(len(l)):
        if l[i].isdigit():
            numero+=1
            
    if especial == 1:
        valor_senhas[j]+=-4
    elif especial == 0:
        valor_senhas[j]+=-8
    
    if letram == 1:
        valor_senhas[j]+=-4
    elif letram == 0: 
        valor_senhas[j]+=-8
    
    if letraM == 1:
        valor_senhas[j]+=-4
    elif letraM == 0: 
        valor_senhas[j]+=-8
        
    if numero == 1:
        valor_senhas[j]+=-4
    elif numero == 0: 
        valor_senhas[j]+=-8

for i in range(n):
    total = 0
    l = list(senhas_aux[i])
    for j in range(len(l)):
        if l[j] != ' ':
            if senhas_aux[i].count(l[j]) == 3:
                total += -2
            elif senhas_aux[i].count(l[j]) == 4:
                total += -4
            elif senhas_aux[i].count(l[j]) >= 5:
                total += -8
        senhas_aux[i] = senhas_aux[i].replace(l[j],' ')
    valor_senhas[i] += total

forca=['']*n
for i in range(n):
    if valor_senhas[i]>=10:
        forca[i]="{}: Forte ({})".format(senhas[i],str(valor_senhas[i]))
    elif valor_senhas[i]>=0 and valor_senhas[i]<10:
        forca[i]="{}: Suficiente ({})".format(senhas[i],str(valor_senhas[i]))
    elif valor_senhas[i]>=-20 and valor_senhas[i]<0:
        forca[i]="{}: Fraca ({})".format(senhas[i],str(valor_senhas[i]))
    elif valor_senhas[i]<-20:
        forca[i]="{}: Insuficiente ({})".format(senhas[i],str(valor_senhas[i]))

for i in range(n):  
    print(forca[i])
    