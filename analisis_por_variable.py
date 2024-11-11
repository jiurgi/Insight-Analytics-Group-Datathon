import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
from scipy import stats


#Función para realizar tablas de frecuencia (Cualitativas)
def tabla_frecuencia_cualitativa(data: pd.DataFrame, column:str):
    frecuencia_absoluta = data[column].value_counts()
    frecuencia_relativa = data[column].value_counts(normalize = True)
    tabla_frecuencias = pd.DataFrame({"Frecuencia Absoluta": frecuencia_absoluta,
                                      "Frecuencia Relativa": frecuencia_relativa})
    return tabla_frecuencias
    

#Función para calcular las medidas de tendencia central de las variables cuantitativas
def medidas_de_tendencia_central(data:pd.DataFrame, column:str):
    media = data[column].mean() 
    mediana = data[column].median()
    moda = stats.mode(data[column], keepdims=True)[0][0]
    
    return f"\nMedia: {media}\nMediana: {mediana}\nModa: {moda}"


#Función para calcular las medidas de variabilidad de las variables cuantitativas
def medidas_de_variabilidad(data:pd.DataFrame, column:str):
    media = data[column].mean() 
    valores_unicos = data[column].nunique()
    minimo = data[column].min()
    maximo = data[column].max()
    varianza = data[column].var()
    desviacion_estandar = data[column].std()
    rango = data[column].max() - data[column].min()
    coeficiente_variacion = (desviacion_estandar / media) * 100
    return (f"\nValores Únicos: {valores_unicos}\nMáximo: {maximo}\nMínimo: {minimo}\n"
            f"Varianza: {varianza}\nDesviación Estándar: {desviacion_estandar}\n"
            f"Rango: {rango}\nCoeficiente de Variación: {coeficiente_variacion}")


#Función para calcular las medidas de forma de las variables cuantitativas
def medidas_de_forma(data:pd.DataFrame, column:str):
    coef_asimetria = stats.skew(data[column])
    coef_curtosis = stats.kurtosis(data[column])
    return f"\nCoeficiente de Asimetría: {coef_asimetria}\nCoeficiente de Curtosis: {coef_curtosis}"


#Función para generar un informe estadístico de la variable 
def informe(data: pd.DataFrame, column: str):
    # Definir el tamaño del título y calcular espacios para centrar
    title_size = 30
    title_centralizado = f"{'MEDIDAS DE TENDENCIA CENTRAL':^{title_size}}"
    print(title_centralizado)
    print(medidas_de_tendencia_central(data, column))

    title_centralizado = f"\n{'MEDIDAS DE VARIABILIDAD':^{title_size}}"
    print(title_centralizado)
    print(medidas_de_variabilidad(data, column))

    title_centralizado = f"\n{'MEDIDAS DE FORMA':^{title_size}}"
    print(title_centralizado)
    print(medidas_de_forma(data, column))
    

#Función para calcular los cuartiles de las variables cuantitativas
def percentiles(data:pd.DataFrame, column:str):
    cuartil_1 = data[column].quantile(0.25) 
    cuartil_2 = data[column].quantile(0.50)  
    cuartil_3 = data[column].quantile(0.75)  
    valor_maximo = data[column].max()
    

    cuartiles = pd.DataFrame({"Primer_cuartil": cuartil_1,
                              "Segundo_cuartil": cuartil_2,
                              "Tercer_cuartil": cuartil_3,
                              "Máximo": valor_maximo}, index=[0])

    return cuartiles


#Función para calcular la tabla de frecuencias de las variables cuantitativas
def frecuencias(data:pd.DataFrame, column: str):
    n = len(data[column])

    # Regla de Sturges: calcular el número óptimo de intervalos
    k = math.ceil(1 + 3.322 * math.log10(n))

    # Crear los intervalos
    # Usamos np.histogram para calcular los límites de los intervalos automáticamente
    frequencies, bins = np.histogram(data[column], bins=k)

    # Crear un DataFrame con la tabla de frecuencias
    table = pd.DataFrame({
        'Intervalo': pd.IntervalIndex.from_breaks(bins),
        'Frecuencia Absoluta': frequencies,
        'Frecuencia Acumulada': np.cumsum(frequencies),
        'Frecuencia Relativa': frequencies / n,
        'Frecuencia Relativa Acumulada': np.cumsum((frequencies/n))
    })
    return table