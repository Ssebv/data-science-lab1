import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV en un DataFrame
medicion1 = pd.read_csv('datos_experimento_1.csv')
medicion2 = pd.read_csv('datos_experimento_2.csv')

estudio = [medicion1,medicion2]

# Calcular estadísticas descriptivas
def medidas(df,colName):
    mean_value = df[colName].mean()
    std_value = df[colName].std()
    max_value = df[colName].max()
    min_value = df[colName].min()
    listado = [mean_value,std_value, max_value, min_value]
    return listado

l = ["Timestamp","Idle Time","Memory Usage","Bytes Sent","Bytes Received"]

for caso in estudio:
    for i in l:
        resultados = medidas(caso,i)
        print("Categoría:", i, "\n",
            "Media:", resultados[0],"\n",
            "Desviación estándar:", resultados[1],"\n",
            "Máximo:", resultados[2], "\n",
            "Mínimo:", resultados[3], "\n")
    

# Visual medidas de analisis descriptivo
for Caso in estudio:
    for col in l:
        plt.plot(Caso[col], marker='o')
        plt.xlabel(col)
        plt.ylabel('Valor')
        plt.title('Gráfico')
        plt.grid(True)
        plt.show()