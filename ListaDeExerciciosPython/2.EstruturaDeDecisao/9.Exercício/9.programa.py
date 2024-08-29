# Faça um Programa que leia três números e mostre-os em ordem decrescente.

# Digite 3 números:
a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
c = int(input("Digite um número: "))

# Imprimir o resultado
if a >= b and a >= c and b >= c:
    print("A ordem decrescente é {}, {}, {}".format(a,b,c))
elif a >= b and a >= c and c >= b:
    print("A ordem decrescente é {}, {}, {}".format(a,c,b))
elif b >= a and b >= c and a >= c:
    print("A ordem decrescente é {}, {}, {}".format(b,a,c))
elif b >= a and b >= c and c >= a:
    print("A ordem decrescente é {}, {}, {}".format(b,c,a))
elif c >= a and c >= b and a >= b:
    print("A ordem decrescente é {}, {}, {}".format(a,c,b))
elif c >= a and c >= b and b >= a:
    print("A ordem decrescente é {}, {}, {}".format(c,b,a))