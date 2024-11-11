import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
from scipy import stats

def matriz_de_var_and_cov(data:pd.DataFrame):
    cov_matrix = data.cov()
    return cov_matrix

def matriz_de_corr(data:pd.DataFrame):
    correlation_matrix = data.corr()
    return correlation_matrix

def grafico_corr(data:pd.DataFrame):
    corr = matriz_de_corr(data)
    plt.figure(figsize=(8, 6))  # Ajustar el tamaño de la figura
    sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Matriz de Correlaciones')
    plt.show()

def correlograma(data:pd.DataFrame):
    sns.pairplot(data)
    plt.suptitle("Correlograma", y=1.02)  
    plt.show()

def grafico_pares(data:pd.DataFrame, column:str):
    sns.pairplot(data, hue=column)  
    plt.suptitle("Correlograma por Estaciones", y=1.02) 
    plt.show()
