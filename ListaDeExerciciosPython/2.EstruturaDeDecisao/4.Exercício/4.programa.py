# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

# Digite uma letra
letra = str(input("Digite uma letra: ")).strip().upper()[0].lower()

# Condição
if letra in ('a','e','i','o','u'):
    print("A letra digitado é uma vogal.")
elif letra in ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
    print("A letra digitada é uma consoante.")
else:
    print("Não é vogal nem consoante.")