#creando una funcion lambda x : x*2

multiplicar_por_dos = lambda x : x*2

# creando una funcion comun que diga si es par o ndo
numeros = [2,4,5,6,1,2,3,54,6,2,1]

def es_par(num):
    if (num % 2 == 0):
        return True 
    
#usando una funcion filter
numeros_pares = filter(es_par, numeros)

print(list(numeros_pares))# tenes que pasarle list, para identificar

#creando una funcion lambda para filtrar

numeros_pares_lambda = filter(lambda numero: numero %2 == 0, numeros)
print(list(numeros_pares_lambda))