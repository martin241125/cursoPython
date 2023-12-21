frutas = [
    'frutilla',
    'anana',
    'manzana',
    'banana',
    'pera',
    'naranja',
    'durazno'
]

texto = 'hola martin?'

edades = [25, 23, 32, 10]

for fruta in frutas:
    if fruta == 'anana':
        continue
    print(f'Me voy a comer una {fruta}')
    
    
for fruta in frutas:
    if fruta == 'anana':
        break
    print(f'Me voy a comer una {fruta}')
else:
    print('terminado')
    


for letra in texto:
    print(letra)
    
#for en 1 linea de codigo

numeros_duplicados = [x*2 for x in edades]

print(numeros_duplicados)