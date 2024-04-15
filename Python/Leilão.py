# Solicita ao usuário o valor inicial da oferta
oferta = float(input())
oferta_min = oferta
nome_passado = ""  # Variável para armazenar o nome do último participante que fez o lance mais alto
print("Lance mínimo: R$ {}.".format("%.2f" % oferta_min))

# Loop infinito para o leilão
while True:
    nome = str(input())  # Solicita o nome do participante
    if nome != "FIM":  # Se o nome não for "FIM", continua o leilão
        if nome != "PAUSA":  # Se o nome não for "PAUSA", é um lance válido
            lance = float(input())  # Solicita o lance do participante
            if lance > oferta or (oferta == oferta_min and lance == oferta_min):
                # Se o lance for maior que o lance atual ou se for igual ao lance mínimo e ainda não houve lances
                nome_passado = str(nome)  # Atualiza o nome do participante que fez o lance mais alto
                oferta = lance  # Atualiza o valor da oferta
        else:
            if nome_passado == "":
                print("Alguém oferece o lance mínimo?")  # Se não houve lances, solicita o lance mínimo novamente
            else:
                print("Maior oferta até agora: R$ {}. Alguém oferece mais?".format("%.2f" % oferta))
                # Se houve lances, solicita lances adicionais
    else:
        if nome_passado == "":  # Se não houve lances, exibe uma mensagem indicando que o item não foi vendido
            print("Dou-lhe uma, dou-lhe duas, dou-lhe três!")
            print("O item não foi vendido. Anunciaremos um novo leilão em breve.")
            break
        else:
            print("Dou-lhe uma, dou-lhe duas, dou-lhe três!")
            print("Vendido para {} por R$ {}!".format(nome_passado, "%.2f" % oferta))
            # Se houve lances, exibe uma mensagem indicando o vencedor do leilão e o valor final
            break
