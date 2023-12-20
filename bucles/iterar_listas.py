animales = [ 'gato',
    'perro',
    'gato',
    'cocodrilo']

numeros = [52, 32, 16, 10]

#recorriendo la lista animales
for animal in animales:
    print(f'ahora la variable anima es igual a {animal}')
    
#recorriendo la lista numeros y sumamos 10 al valor

for numero in numeros:
    resultado = numero + 10
    print(resultado)

#recorriendo 2 litas al mismo tiempo

for numero, animale in zip(numeros, animales):
    print(f'recorriendo lista 1: {animal}')
    print(f'recorriendo lista 2: {numero}')
    

#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es {indice} y el valor es {valor}')
    
#usando el else
for nume in numeros:
    print(f'ejecutando el ultimo bucle, valor actual: {nume}')
else:
    print('aca termina')