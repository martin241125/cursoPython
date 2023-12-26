cadena1 = 'jose,martin,miño'
cadena2 = 'esta casado'



busqueda_numero = lista.index

# conver mayusculas
cadena1.upper()

# conver minusculas
cadena1.lower()

# conver 1er mayus
cadena1.capitalize()

# buscamamos caracter en una cadena
busqueda_find = cadena2.find('casado')

# buscamamos caracter en una cadena, sino hay coincidencia lanza una excepcion
busqueda_find = cadena2.index('casado')

#si es un dato numerico, devuelve true sino false
es_numerico = cadena1.isnumeric()

#si es alfanumerico devolvemos true, sino false
es_numerico = cadena1.isalpha()

#buscamos un caracter en una cadema y devuelve cuantas veces esta repetido.
contar_coincidencias = cadena1.count('m')

#devuelve la cantidad de caracteres en una cadena de string.
contar_caracter = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, devolvera true sino false.
empieza_con = cadena1.startswith('j')

#verificamos si una cadena termina con otra cadena dada, devolvera true sino false.
empieza_con = cadena1.endswith('j')

#remplaza un pedazo de la cadena dada, con otra dada. toma como parametro el valor anterior y toma otro valor por el cual lo remplazara.
cadena_nueva = cadena1.replace(',', ' ')

#separar cadena con la cadena que le pasemos
separar_cadena = cadena1.split(',')

print(separar_cadena)