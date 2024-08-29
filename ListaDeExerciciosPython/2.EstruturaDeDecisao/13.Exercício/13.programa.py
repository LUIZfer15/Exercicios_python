# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

# Digite um número
dia_int = int(input("Digite um número do dia da semana: "))

# Condição
if dia_int == 1:
    print("O dia correspondente é Domingo")
elif dia_int == 2:
    print("O dia correspondente é Segunda")
elif dia_int == 3:
    print("O dia correspondente é Terça")
elif dia_int == 4:
    print("O dia correspondente é Quarta")
elif dia_int == 5:
    print("O dia correspondente é Quinta")
elif dia_int == 6:
    print("O dia correspondente é Sexta")
elif dia_int == 7:
    print("O dia correspondente é Sabádo")
elif dia_int == 0 or dia_int >= 8:
    print("Número Inválido!")