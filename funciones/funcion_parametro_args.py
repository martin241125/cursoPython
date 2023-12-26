# sumar valores con varios argumentos
def suma_total(numeros): #toma numeros de parametros
    return sum([*numeros]) #utilizamos la funcion sum prestablezida y le ponemos * que es muchos args y los suma

resultado = suma_total([5,5,4,6,8])

print(resultado)

#lo mismo de arriba pero utilizando el operador * como parametro args

def suma(nombre, *numeros):
    return f'{nombre}, la suma de tus numeros es: {sum(numeros)}'

resultado2 = suma('Martin', 5,1,3)

print(resultado2)