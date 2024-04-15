# Solicita ao usuário que entre com o objeto e o tamanho
obj = str(input())
size = int(input())

# Verifica se o objeto é um dos tipos válidos e se o tamanho está dentro de limites específicos
if (obj == "TD") or (obj == "TE") or (obj == "TS") or (obj == "TI") or (obj == "L"):
    if size > 0 and size < 10:

        # Se o objeto for uma pirâmide equilátera (TE)
        if obj=="TE":
            for i in range(size+1):
                l1=range(i+1)
                print((size-i)*" "+str("".join(str(e) for e in l1)))
            for i in range(size):
                l1=range(size-i)
                print((i+1)*" "+str("".join(str(e) for e in l1)))

        # Se o objeto for uma pirâmide invertida (TD)
        elif obj=="TD":
            for i in range(size+1):
                l1=range(i+1)
                print(str("".join(str(e) for e in l1[::-1])))
            for i in range(size):
                l1=range(size-i)
                print(str("".join(str(e) for e in l1[::-1])))

        # Se o objeto for um triângulo de Sierpinski (TS)
        elif obj=="TS":
            for i in range(size+1):
                l1 = list(range(i+1))
                l2=l1+l1[-2::-1]
                print((size-i)*" "+str("".join(str(e) for e in l2)))

        # Se o objeto for um triângulo invertido (TI)
        elif obj=="TI":
            for i in range(size+1):
                l1 = list(range(size-i+1))
                l2=l1+l1[-2::-1]
                print((i)*" "+str("".join(str(e) for e in l2)))

        # Se o objeto for um losango (L)
        elif obj=="L":
            for i in range(size+1):
                l1 = list(range(i+1))
                l2=l1+l1[-2::-1]
                print((size-i)*" "+str("".join(str(e) for e in l2)))
            for i in range(size):
                l1 = list(range(size-i))
                l2=l1+l1[-2::-1]
                print((i+1)*" "+str("".join(str(e) for e in l2)))

    # Se o tamanho não estiver dentro dos limites permitidos
    else: print("Numero maximo invalido.")

# Se o objeto não for um dos tipos válidos
else: print("Objeto invalido.")
