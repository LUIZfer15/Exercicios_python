# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

# Variável
limite = 50
excesso = 0
multa = 4

# Escreva quantos kg tem o peixe
peso = float(input("Digite o peso total dos peixes: "))

# Condição
if peso>limite:
    excesso = peso-limite
    multa = excesso * multa
    print("Peso acima do limite de {}kg".format(limite))
    print("O valor da multa é de R$ {:.2f} pelo excesso de {:.2f} kg.".format(multa,excesso))
else:
    print("Peso aceito, está abaixo do limite de {} kg!".format(limite))