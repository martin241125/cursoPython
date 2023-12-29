#programa que te devulve un saludo

def frase(nombre,edad:int,casado:bool = False):
    if casado == True:
        return f'Hola {nombre} tienes {edad} de edad y te encuentras casado'
    else:
        return f'Hola {nombre} tienes {edad} de edad y te encuentras soltero'



