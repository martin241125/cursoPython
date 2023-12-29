#listas, una con nombres otra con apellidos.

nombres= ['martin', 'cecilia', 'josefina', 'mirta','ruben']
apellidos= ['miño','bustamante','cabral','carlox','curry']

with open('archivos_problemas\\nombres_y_apellidos.txt', 'w', encoding='UTF-8') as archi:
    archi.writelines('Los datos son:\n')
    [archi.writelines(f'Nombres: {n}\nApellidos: {a}\n-----\n') for n,a in zip(nombres, apellidos)]