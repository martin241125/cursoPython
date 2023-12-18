#ejercicio 2
frase = input('dime una frase y calculare cuanto tardarias en decirlo: ')
palabras_separadas = frase.split(' ')
cantidad_de_palabras = len(palabras_separadas)

print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo')