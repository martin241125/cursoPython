import pandas as pd

#leyendo archivo

df = pd.read_csv('archivos\\datos.csv', encoding='UTF-8')

#obtiene los datos de una columna especifica
nombre = df['nombre']


#slide
cadena = '0123456789'
print(cadena[0:5])

#ordenando el dataframe por edad

df_ordenado = df.sort_values('edad', ascending=False) #agregandole ascendig podemos ordenar de mayor a menor


#accediendo a las primeras filas con head()
primeras_filas = df.head()

#accediendo a las ultimas filas con tail()
ultimas_filas = df.tail()


#obteniendo la cantidad de filas y las columnas con shape
filas_totales, columnas_totales = df.shape

#obteniendo data estadistica del dataframe
df_info = df.describe()

#accediendo a un elemento especifico del df con loc
elemento_especifico_loc = df.loc[1,"edad"]

#accediendo a la edad de la fila 1 con iloc
elemento_especifico_loc = df.iloc[1,2]

#accediendo a todas las filas de una columna
apellido = df.iloc[:,1]

#accediendo a la fila 3 con iloc
fila_1 = df.iloc[1,:]


print(fila_1)


