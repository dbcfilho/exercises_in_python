n = int(input("Digite o valor de n: "))

if n < 0:
    print("Fatorial não definido para números negativos.")
else:
    resultado = 1
    i = 1
    if n == 0:
        resultado = 1
    else:
        while i <= n:
            resultado *= i
            i += 1

    print(resultado)