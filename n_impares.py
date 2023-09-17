n = int(input("Digite o valor de n: "))

if n <= 0:
    print("Digite um número inteiro positivo maior que zero.")
else:
    numero = 1
    contador = 0
    
    while contador < n:
        if numero % 2 != 0:
            print(numero)
            contador += 1
        numero += 1