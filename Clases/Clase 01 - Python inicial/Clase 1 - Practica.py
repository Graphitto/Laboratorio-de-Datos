# Clase 1 - Practica -- Labo de Datos (15/08)

# Ejercicio 1 -- Ver si palabra es palindromo
'''
word = input('Ingrese una palabra: ')
palindromo = True

for i in range(len(word)//2):
    # palindromo = palindromo and (word[i] == word[len(word)- i - 1])
    if word[i] != word[len(word)- i - 1]:
        palindromo = False
        break
    
print(palindromo) # '''

# Ejercicio 2 -- Numeros enteros entre 0 y 213 que sean divisibles por 13
'''
limite = 213
div = 13
res = []

for i in range(limite):
    if (i%div == 0):
        res += [i]

print(res) # '''

# Ejercicio 3 -- Apilar billetes en el obelisco
'''
altura_obelisco = 67500
altura_actual = 0.11 / 10
res = 1

while altura_actual < altura_obelisco:
    altura_actual *= 2
    res += 1

print(res) # '''
# print(f'Se necesitan {res} dias y la altura final es {altura_actual}') 

# Ejemplos de range(x)
'''
for x in range(5): # (inicio = 0, fin, paso = 1)
    print(x)
print('')

for x in range(0, 5, 1): # (inicio, fin, paso)
    print(x)
print('')

for x in range(-5, -1): # (inicio, fin)
    print(x)
print('')

# '''

# Ejercicio 4 -- Geringoso
'''
cadena = 'Geringoso'
capadepenapa = ''

for c in cadena:
    if c in {'a','e','i','o','u'}:
        capadepenapa += (c + 'p' + c)
    else:
        capadepenapa += c

print(capadepenapa) # '''

# Ejercicio 5 -- Rebotes de pelota
'''
altura_actual = 100
iteraciones = 10

while iteraciones > 0:
    altura_actual *= 0.6
    iteraciones -= 1

print(altura_actual) # '''

# Ejercicio 6 -- Funciones
'''
def maximo(a, b):
    if a > b:
        return a
    else:
        return b
    # a if a > b else b # (forma corta)
    
def tachar_pares(lista):
    res = []
    for i in range(len(lista)):
        if lista[i] % 2 == 1:
            res += [str(lista[i])]
        else:
            res += ['x']
    return res

print(maximo(5,1))
print(tachar_pares([1,2,3,4,5,6])) # '''

