# Faça um Programa que peça dois números e imprima o maior deles.

# Digite um número
n1 = int(input("Digite um número: "))

# Digite outro número
n2 = int(input("Digite outro número: "))

# Condição
if n1>n2:
    print("O maior valor digitado é {:.0f}".format(n1))
else:
    print("O maior valor digitado é {:.0f}".format(n2))