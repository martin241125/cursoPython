#abrimos el archivo

with open('archivos\\texto.txt') as archivo:
    #leemos el archivo
    print(archivo.read())
    print('hola')