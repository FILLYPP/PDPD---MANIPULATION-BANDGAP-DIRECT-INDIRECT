from pandas import read_csv
import matplotlib.pyplot as plt

df = read_csv('resultados.csv')
print(df)
print("test")

df.plot(x='Átomo',y='Energia')
#plt.show()

plt.savefig('./test.png')
