numero = int(input("Digite um número inteiro: "))
tem_adjacente_igual = False

while numero > 0:
    digito_atual = numero % 10
    numero //= 10
    
    if numero % 10 == digito_atual:
        tem_adjacente_igual = True
        break

if tem_adjacente_igual:
    print("sim")
else:
    print("não")