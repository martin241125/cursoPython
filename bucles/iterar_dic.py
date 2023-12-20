diccionario = {
    'nombre': 'martin',
    'apellido': 'miño',
    'edad' : 32
}

for key in diccionario.items():
    indice = key[0]
    valor = key[1]
    print(f'el dato es {indice} y su valor es {valor}')