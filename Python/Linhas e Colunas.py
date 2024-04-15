# Solicita ao usuário o número de linhas e colunas da matriz
r = int(input())
c = int(input())

# Lista para armazenar as linhas da matriz
linhas = []
for i in range(r):
    a = [int(x) for x in input().split()]  # Lê uma linha de entrada do usuário e divide em valores inteiros
    linhas.append(a)

# Calcula o número de linhas e colunas da matriz de saída (maior devido à representação gráfica)
rn = r * 2 + 1
cn = c * 4 + 1

# Cria uma matriz preenchida com "#" para representar a grade
matrix = []
for i in range(rn):
    matrix.append(["#"] * cn)

# Preenche a matriz com os valores da matriz de entrada e desenha a grade
for i in range(r * 2 + 1):
    for j in range(c * 4 + 1):
        if i != 0 and i != r * 2 and j != 0 and j != c * 4:
            matrix[i][j] = " "  
        if i % 2 == 1 and j % 4 == 2:
            a = int((i - 1) / 2)
            b = int((j - 2) / 4)
            matrix[i][j] = linhas[a][b]

# Desenha as linhas verticais da grade
for i in range(r * 2 + 1):
    for j in range(c * 4 + 1):
        if i % 2 == 1 and j % 4 == 0 and j != 0 and j != c * 4 and matrix[i][j-2] != matrix[i][j+2]:
            matrix[i][j] = "|"

# Desenha as linhas horizontais da grade
for i in range(r * 2 + 1):
    for j in range(c * 4 + 1):
        if i % 2 == 0 and j % 4 == 2 and i != 0 and i != r * 2 and matrix[i-1][j] != matrix[i+1][j]:
            matrix[i][j] = "-"
            matrix[i][j-1] = "-"
            matrix[i][j+1] = "-"

# Adiciona os cantos "+" onde as linhas verticais e horizontais se cruzam
for i in range(r * 2 + 1):
    for j in range(c * 4 + 1):
        if i % 2 == 0 and j % 4 == 0 and j != 0 and j != c * 4 and i != 0 and i != r * 2:
            if (matrix[i+1][j] == "|" and matrix[i][j+1] == "-") or (matrix[i+1][j] == "|" and matrix[i][j-1] == "-") or (matrix[i-1][j] == "|" and matrix[i][j+1] == "-") or (matrix[i-1][j] == "|" and matrix[i][j-1] == "-"):
                matrix[i][j] = "+"
            elif matrix[i+1][j] == matrix[i-1][j] and matrix[i+1][j] != " ":
                matrix[i][j] = "|"
            elif matrix[i][j+1] == matrix[i][j-1] and matrix[i][j+1] != " ":
                matrix[i][j] = "-"

# Imprime a matriz resultante que representa a grade
for x in matrix:
    print(*x, sep="")
