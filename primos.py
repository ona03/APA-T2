def esPrimo(numero):
    return numero > 1 and all(numero % n != 0 for n in range(2,numero))

def primos(numero):
    primos_encontrados = [n for n in range(2, numero) if esPrimo(n)]
    return tuple(primos_encontrados)

# def descompon(numero):
#     factores = []
#     for primo in primos(numero):
#         while numero % primo == 0:
#             factores.append(primo)
#             numero //= primo
#     return tuple(factores)

def descompon(numero):
    factores = []
    divisor = 2
    while numero > 1:
        if numero % divisor == 0 and esPrimo(divisor):
            factores.append(divisor)
            numero //= divisor
        else:
            divisor += 1
    return tuple(factores)

def mcm(numero1, numero2):
    factores_numero1 = descompon(numero1)
    factores_numero2 = descompon(numero2)

    factores_comunes = set(factores_numero1) | set(factores_numero2)

    mcm_resultado = 1
    
    for factor in factores_comunes:
        exponente = max(factores_numero1.count(factor), factores_numero2.count(factor))
        mcm_resultado *= factor ** exponente
    
    return mcm_resultado

def mcd(numero1, numero2):
    factores_numero1 = descompon(numero1)
    factores_numero2 = descompon(numero2)
    
    factores_comunes = set(factores_numero1) & set(factores_numero2)
    
    mcd_resultado = 1
    
    for factor in factores_comunes:
        exponente = min(factores_numero1.count(factor), factores_numero2.count(factor))
        mcd_resultado *= factor ** exponente
    
    return mcd_resultado

def mcmN(*numeros):
    factores_numeros = [descompon(num) for num in numeros]
    
    factores_comunes = set()

    for tupla in factores_numeros:
        factores_comunes.update(tupla)

    max_exponentes = {}
    for factor in factores_comunes:
        max_exponentes[factor] = max(tupla.count(factor) for tupla in factores_numeros)

    mcm_resultado = 1
    for factor, exponente in max_exponentes.items():
        mcm_resultado *= factor ** exponente

    return mcm_resultado

def mcdN(*numeros):
    factores_numeros = [descompon(num) for num in numeros]
    
    factores_comunes = set()

    for tupla in factores_numeros:
        factores_comunes.update(tupla)

    min_exponentes = {}
    for factor in factores_comunes:
        min_exponentes[factor] = min(tupla.count(factor) for tupla in factores_numeros)

    mcd_resultado = 1
    for factor, exponente in min_exponentes.items():
        mcd_resultado *= factor ** exponente

    return mcd_resultado

print("Test 1: " + str([numero for numero in range(2, 50) if esPrimo(numero)]))
print("Test 2: " + str(primos (50)))
print("Test 3: " + str(descompon(36 * 175 * 143)))
print("Test 4: " + str(mcm(90, 14)))
print("Test 5: " + str(mcd(924, 780)))
print("Test 6: " + str(mcmN(42, 60, 70, 63)))
print("Test 7: " + str(mcdN(840, 630, 1050, 1470)))