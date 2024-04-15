from random import randrange

# Gera um número aleatório entre 5 e 10, que determina o tamanho da lista
l1 = randrange(5, 10)

# Gera uma lista de números aleatórios com tamanho l1
n1 = []
for i in range(l1):
    a1 = randrange(0, 1000)
    n1.append(a1)

# Cria cópias da lista original para aplicar diferentes algoritmos de ordenação
n2 = n1[:]
n3 = n1[:]
n4 = n1[:]

# Implementação do algoritmo bubble sort
def bubble_sort(lista):
    k = 1
    for i in range(len(lista)):
        for j in range(len(lista) - k):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
        k += 1
    return lista

# Implementação do algoritmo selection sort
def selection_sort(lista):
    k = 0
    for i in range(len(lista)):
        ind = lista.index(min(lista[k:len(lista)]))
        lista[k], lista[ind] = lista[ind], lista[k]      
        k += 1  
    return lista

# Implementação do algoritmo insertion sort
def insertion_sort(lista):
    for i in range(len(lista)):
        k = i - 1
        while lista[k] > lista[i] and k >= 0:
            lista[i], lista[k] = lista[k], lista[i]
            k -= 1
            i -= 1
    return lista

# Aplica os algoritmos de ordenação e imprime os resultados
print("Bubble....", n1, bubble_sort(n2))
print("Selection.", n1, selection_sort(n3))
print("Insertion.", n1, insertion_sort(n4))
