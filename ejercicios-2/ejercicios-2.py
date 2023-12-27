#falto el profesor y los chicos van a armar la clase.

# 1 alumno es profesor y 1 alumno es asistente

#A- Pedir la edad de los compañeros que vinieron hoy a clases y ordenar los datos de menor a mayor.

#B- el mayor de la clases es el profesor y el menor el asistente, ¿quien es quien?.

def obtener_compañeros(cantidad_de_compañeros):
    compañeros = []
    for i in range(cantidad_de_compañeros):
        nombre = input('ingrese el nombre del compañeros: ')
        edad = int(input('ingrese la edad del compañero: '))
        compañero = (nombre, edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente,profesor

asistente, profesor = obtener_compañeros(4)

print(f'El profesor es: {profesor} y su asistente es {asistente}')