# Faça um Programa que leia três números e mostre o maior e o menor deles.

# Digite 3 números
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

# Variável
max_num = max(n1,n2,n3)
min_num = min(n1,n2,n3)

# Imprimir o resultado
print("O maior número digitado é {}".format(max_num))
print("O menor número digitado é {}".format(min_num))