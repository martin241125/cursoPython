import pandas as pd
import matplotlib.pyplot as  plt
import seaborn as sns

df = pd.read_csv("problemas_graficos\\gastos.csv")
print(df)

sns.lineplot(x="fecha", y="gastos",data=df)

plt.plot('01-04',1500,'o')

plt.show()