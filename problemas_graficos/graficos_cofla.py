import pandas as pd
import matplotlib.pyplot as  plt
import seaborn as sns

df = pd.read_csv("problemas_graficos\\cofla_ingresos.csv")
print(df)

#creando el grafico
sns.barplot(x='fuente', y='ingresos', data=df)

#calculando el ingreso de cofla
total_ingresos = df['ingresos'].sum()

#mostrando los ingresos
print(total_ingresos)

#mostrando el grafico
plt.show()