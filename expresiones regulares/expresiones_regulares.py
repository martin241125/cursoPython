import re

texto = '''Hola como estas martin? tenes 32. , todavia seguis buscando trabajo.
Si, se que esta dificil pero no te rindas.
En enero tenes muchas chances de encontrar trabajo.'''

#haciendo una busqueda simple
#resultado = re.findall('martin', texto,flags=re.IGNORECASE)

#\d -> busca digitos numericos del 0 al 9
#resultado = re.findall(r'\d', texto)

#\D -> busca todo menos  digitos numericos del 0 al 9
#resultado = re.findall(r'\D', texto)

#\w -> busca caracteres alfanumericos [a-z A-Z 0-9 _]
#resultado = re.findall(r'\w', texto)

#\W -> busca todo menos caracteres alfanumericos [a-z A-Z 0-9 _]
#resultado = re.findall(r'\W', texto)

#\s -> busca espacion en blanco -> espacios, tabs, saltos de linea
#resultado = re.findall(r'\s', texto)

#\ -> cancela los caracteres especiales
#resultado = re.findall(r'\.',texto)

# armando una cadena que busque un numero, seguido de un punto y un espacio
#resultado = re.findall(r'\d\.\s', texto)

#buscar el principo de una linea
#flags=re.M activa la multilinea
#resultado = re.findall(f'^Hola', texto)

#buscar el final de cada linea

#resultado = re.findall(r'trabajo$', texto, flags=re.M)

#{n} -> busca n cantidad de veces el valor de la izquierda (e numeros juntos esta vez)
#resultado = re.findall(r'\d{3}', texto)

#{n,m} -> busca n cantidad de veces el valor de la izquierda (e numeros juntos esta vez)
#resultado = re.findall(r'\d{1,4}', texto)

print(resultado)