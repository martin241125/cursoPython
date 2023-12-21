diccionario = {
    'nombre': 'martin',
    'apellido': 'miño',
    'edad' : 32
}

#recorriendo diccionario para obtener la clave 
for key in diccionario:
    key
    
    print(f'el dato es {key}')

#recorriendo diccionario con items() para obtener la clave y el valor
for key in diccionario.items():
    indice = key[0]
    valor = key[1]
    print(f'el dato es {indice} y su valor es {valor}')