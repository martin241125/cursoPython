#creando una funcion simple

def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == 'mujer'):
        print(f'Hola {nombre} como esta mi maestra?')
    elif (sexo == 'hombre'):
        print(f'hola {nombre} como esta mi maestro?  ')
    
saludar('cecilia', 'mujer')

#crear una funcion que nos retorne valor.

def crear_contraseña_random(num):
    chars = "abcdefghijk"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 3
    c2 = num
    c3 = num - 5
    contraseña = f'{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}'
    return contraseña

password = crear_contraseña_random(5)
frase = f'Tu contraseña nueva es: {password}'
print(frase)