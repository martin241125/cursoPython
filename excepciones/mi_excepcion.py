#creando mi propia excepcion perzonalizada

class MiExcepcion(Exception):
    def __init__(self,err):
        print(f'Cometiste el siguiente error: {err}')

#manejandola
try:        
    raise MiExcepcion('Utiliza un valor correcto pa!')
except:
    print('Trata de escribir un valor correcto!')