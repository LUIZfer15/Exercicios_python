# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

# Digite "F" ou "M"
sexo = str(input("Informe seu sexo: [M/F] ")).strip().upper()[0]

# Condição
while sexo not in "MmFf":
    sexo = str(input("Dados inválidos. Por favor, informe seu sexo: ")).strip().upper()[0]
    
# Imprimir resultado
print("Sexo {} registrado com sucesso!".format(sexo))