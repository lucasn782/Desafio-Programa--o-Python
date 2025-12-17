def fatores_primos(numero):
    fatores = []
    divisor = 2
    while divisor <= numero:
        if numero % divisor == 0:
            fatores.append(divisor)
            numero = numero // divisor
        else:
            divisor += 1
    return fatores
