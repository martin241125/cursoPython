#creando una lista con list()
lista = list(['jose', 'martin', 32])
print(lista)
#len devuelve la cantidad de elementos en la lista
rta = len(lista)

#agregando un elemento a la lista
lista.append('casado')

#agrega un elemento a una lista, en una posicion especifica
lista.insert(2, "josefina")

# agregando varios elementos a la lista, los agrega por al final
lista.extend(['cecilia', True])

# eliminando un elemento de la lista, por el indice, muta la lista, despues de pop. con -1 eliminamos el ultimo elemento de la lista.
lista.pop(0)

#removiendo un elemento de la lista por su valor.
lista.remove('casado')

#elimina todos los elementos de la lista
#lista.clear()

#ordena la lista pero numerica, no acepta cadenas.
lista.sort() #reverse=True, lo hace al revez.

#invierte los elementos de una lista.
lista.reverse()

print(lista)
