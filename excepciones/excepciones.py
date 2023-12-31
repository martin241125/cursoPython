#creando una funcion 
def dividiendo():
    #iniciando un bucle
    while True:
        #pidiendo los numeros
        a = input('Nº 1 : ')
        b = input('Nº 2 : ')
        #abrimos un try, y convertimos a enteros los numeros
        try:
            resultado = int(a) / int(b)
        #si lanzo una excepción, pedirle que reingrese los datos
        except:
            print('Solo aceptamos numeros.')
        #si todo salio bien terminamos el bucle    
        else:
            break
        finally:
            print('manejo de excepción finalizado')
    #mostrando el resultado
    return resultado

print(dividiendo())