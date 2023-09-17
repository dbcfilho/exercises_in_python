numero = int(input("Digite um número inteiro: "))
e_primo = True

if numero <= 1:
    e_primo = False
else:
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            e_primo = False
            break
        divisor += 1

if e_primo:
    print("primo")
else:
    print("não primo")
