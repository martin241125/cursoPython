diccionario = {
    'nombre' : 'martin',
    'apellido' : 'miño',
    'edad' : 32
}
#me muestras las claves del diccionario
claves = diccionario.keys() 

#conociendo las claves puedo acceder a su valor
claves2 = diccionario.get('nombre') 

#elimina todos los elementos del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
claves3 = diccionario.pop('edad')

print(claves)
print(claves2)
print(claves3) # me muestra el elemento eliminado