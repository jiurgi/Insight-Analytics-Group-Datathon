import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
from scipy import stats
from analisis_por_variable import frecuencias

def box_plot(data:pd.DataFrame, column:str):

    flierprops = dict(marker='o', markerfacecolor='red', markersize=8, linestyle='none')  # Outliers en rojo
    medianprops = dict(color='black', linewidth=2) 

    plt.figure(figsize=(8, 6))
    boxplot = plt.boxplot(data[column], vert=False, patch_artist=True, flierprops=flierprops, medianprops=medianprops)
    
    outlier_data = boxplot['fliers'][0].get_data()
    outlier_values = outlier_data[0] 

    for outlier in outlier_values:
        plt.text(outlier, 1.02, f'{outlier}', horizontalalignment='center', color='red', fontsize=12)

    plt.title('Boxplot con Identificación de Outliers', fontsize=14)
    plt.xlabel(column, fontsize=12)

    return plt.show()

def histograma_curva_densidad(data:pd.DataFrame, column:str):
    table = frecuencias(data, column)
    bins = [interval.mid for interval in table['Intervalo']]
    frequencias = table['Frecuencia Absoluta'].values

    # Expandir los datos para el histograma y el gráfico de densidad
    expanded_data = []
    for interval, freq in zip(table['Intervalo'], frequencias):
        start, end = interval.left, interval.right
        expanded_data.extend(np.random.uniform(start, end, freq))

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.hist(expanded_data, bins=len(table['Intervalo']), edgecolor='black', alpha=0.7, color='blue')
    plt.title('Histograma')
    plt.xlabel(column)
    plt.ylabel('Frecuencia')
    plt.show()

    # Gráfico de Densidad
    plt.subplot(1, 2, 2)
    sns.kdeplot(expanded_data, bw_adjust=0.5, fill=True, color='green')
    plt.title('Gráfico de Densidad')
    plt.xlabel(column)
    plt.ylabel('Densidad')

    media = data[column].mean() 
    mediana = data[column].median()
    moda = stats.mode(data[column], keepdims=True)[0][0]

    plt.axvline(media, color='red', linestyle='--', label=f'Media: {media:.2f}')
    plt.axvline(mediana, color='green', linestyle='-.', label=f'Mediana: {mediana:.2f}')
    plt.axvline(moda, color='orange', linestyle=':', label=f'Moda: {moda}')

    plt.legend(title='Medidas de Tendencia Central', loc='best')
    plt.tight_layout()
    plt.show()