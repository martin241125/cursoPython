# creando diccionarios con dict()

diccionario = dict(
    nombre = 'Martin',
    apellido = 'Miño')
     # de esta forma tambien podemos crear dict vacios

rta = diccionario.keys()
rta2 = diccionario.get('nombre')

print(rta, rta2)