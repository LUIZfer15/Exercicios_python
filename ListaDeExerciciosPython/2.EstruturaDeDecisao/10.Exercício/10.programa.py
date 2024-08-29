# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

# Pergunta
turno = str(input("Em qual turno você estuda [M/V/N]? "))

# Condição
while turno not in "MmVvNn":
    turno = str(input("Valor Inválido. Por favor, digite novamente: "))
    
# Imprimir resultado
if turno in "Mm":
    print("Bom Dia!")
elif turno in "Vv":
    print("Boa Tarde!")
elif turno in "Nn":
    print("Boa Noite!")