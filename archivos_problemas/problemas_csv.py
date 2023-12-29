#cambiar el tipo de dato de una columna

import pandas as pd

df = pd.read_csv('archivos_problemas\\datos.csv')

#convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)

#mostrando el tipo de dato del primer elemento de la columna
print(type(df['edad'][0]))

df['apellido'].replace('Mario', "maestro", inplace=True)

#eliminando las filas con datos faltantes
df = df.dropna()

#eliminando las filas repetidas
df = df.drop_duplicates()

print(df)