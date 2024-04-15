# Solicita ao usuário que entre com o nome do mês
mes = input()
dias = 0

# Determina o número de dias do mês com base no nome do mês inserido
if mes == 'janeiro':
    dias = 31
elif mes == 'fevereiro':
    dias = 28
elif mes == 'março':
    dias = 31
elif mes == 'abril':
    dias = 30
elif mes == 'maio':
    dias = 31
elif mes == 'junho':
    dias = 30
elif mes == 'julho':
    dias = 31
elif mes == 'agosto':
    dias = 31
elif mes == 'setembro':
    dias = 30
elif mes == 'outubro':
    dias = 31
elif mes == 'novembro':
    dias = 30
elif mes == 'dezembro':
    dias = 31
else:
    print("Erro")

# Lista vazia para armazenar as vendas de CDs e livros
lista_cds = []
lista_lvs = []
lista_its = []

# Loop para inserir as vendas de CDs e livros para cada dia do mês
for i in range(dias):
    itens = input().split(",")  # Lê a entrada do usuário e separa por vírgulas
    cd = int(itens[0])  # Extrai o número de CDs vendidos
    lv = int(itens[1])  # Extrai o número de livros vendidos
    lista_cds.append(cd)  # Adiciona o número de CDs vendidos à lista
    lista_lvs.append(lv)  # Adiciona o número de livros vendidos à lista

# Calcula o total de itens vendidos (CDs + livros) para cada dia e armazena em uma lista
for i in range(len(lista_cds)):
    it = lista_cds[i] + lista_lvs[i]
    lista_its.append(it)

# Encontra o maior número de CDs vendidos e o dia correspondente
max_cds = lista_cds[0]
dia_max_cds = 1
for i in range(len(lista_cds)):
    if lista_cds[i] > max_cds:
        max_cds = lista_cds[i]
        dia_max_cds = i + 1

# Encontra o maior número de livros vendidos e o dia correspondente
max_lvs = lista_lvs[0]
dia_max_lvs = 1
for i in range(len(lista_lvs)):
    if lista_lvs[i] > max_lvs:
        max_lvs = lista_lvs[i]
        dia_max_lvs = i + 1

# Encontra o maior número total de itens vendidos e o dia correspondente
max_its = lista_its[0]
dia_max_its = 1
for i in range(len(lista_its)):
    if lista_its[i] > max_its:
        max_its = lista_its[i]
        dia_max_its = i + 1

# Imprime os melhores dias de venda para CDs, livros e itens
print("Melhores dias de venda em {}".format(mes))
print("CDs:", dia_max_cds)
print("Livros:", dia_max_lvs)
print("Itens:", dia_max_its)
