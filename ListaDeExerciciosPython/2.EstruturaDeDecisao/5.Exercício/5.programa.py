# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

# Digite duas notas
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

# Variável
media = n1+n2/2

# Resultado da média
print("Sua média é {:.1f}".format(media))

# Condição
if media>=7:
    print("Aprovado!")
elif media==10:
    print("Aprovado com Distinção")
else:
    print("Reprovado")