with open('archivos\\texto.txt','w') as archivo:
    #sobrescribiendo el archivo
    archivo.write('martin estas casado.')
    print(archivo.read())