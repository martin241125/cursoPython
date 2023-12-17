#AND (si las dos condiciones se cumplen devuelve true, sino false)
rta = True & True #devuelve true
rta2 = False & True # devuelve falso
rta3 = True & False # devuelve falso
rta4 = False & False # devuelve falso


#OR (si algunas de las condiciones se cumple devuelve true, si las 2 condiciones son false devolvera false)
rta5 = True | True # devuelve true
rta6 = False | True # devuelve true
rta7 = True | False # devuelve true
rta8 = False | False # devuelve false


#NOT invierte el valor
rta9 = not True # devuelve false
rta10 = not False # devuelve true

edad = 18
edad_registrada = 18

dni = 36544817
dni_registrado = 36544817

if edad == edad_registrada and dni == dni_registrado:
    print('accediendo')
else:
    print('sin acceso')