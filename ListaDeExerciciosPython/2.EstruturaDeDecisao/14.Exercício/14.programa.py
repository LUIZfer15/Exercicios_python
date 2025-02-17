# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  # Média de Aproveitamento  Conceito
  # Entre 9.0 e 10.0        A
  # Entre 7.5 e 9.0         B
  # Entre 6.0 e 7.5         C
  # Entre 4.0 e 6.0         D
  # Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

# Digite as notas
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

# Calculo da média
media = n1+n2/2

# Imprimir o resultado
if media >= 9:
    print("A sua média é {:.1f} e o conceito corresponde a A".format(media))
    print("APROVADO!")
elif media >= 7.5:
    print("A sua média é {:.1f} e o conceito corresponde a B".format(media))
    print("APROVADO!")
elif media >= 6:
    print("A sua média é {:.1f} e o conceito corresponde a C".format(media))
    print("APROVADO!")
elif media >= 4:
    print("A sua média é {:.1f} e o conceito corresponde a D".format(media))
    print("REPROVADO!")
else:
    print("A sua média é {:.1f} e o conceito corresponde a E".format(media))
    print("REPROVADO!")