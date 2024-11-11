# -*- coding: utf-8 -*-
"""ProcesamientoDatosMigracion.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1M_hO_dxLedYTHkXjrHzbRRCF55YLefeD
"""

import pandas as pd

# Lee el archivo Parquet
df2014 = pd.read_parquet('/content/2014.parquet')
df2015 = pd.read_parquet('/content/2015.parquet')
df2016 = pd.read_parquet('/content/2016.parquet')
df2017 = pd.read_parquet('/content/2017.parquet')
df2018 = pd.read_parquet('/content/2018.parquet')
df2019 = pd.read_parquet('/content/2019.parquet')
df2021 = pd.read_parquet('/content/2021.parquet')
df2022 = pd.read_parquet('/content/2022.parquet')
df2023 = pd.read_parquet('/content/2023.parquet')
df2024 = pd.read_parquet('/content/2024 (1).parquet')

import pandas as pd
import numpy as np

# Reemplazar "sin especificar" con NaN
df2014.replace("Sin Especificar", np.nan, inplace=True)

# Eliminar filas que tengan NaN en cualquier columna
df2014 = df2014.dropna()

# Mostrar las primeras filas del DataFrame limpio para verificar
print(df2014.head())

import pandas as pd
import numpy as np

# Reemplazar "sin especificar" con NaN
df2015.replace("Sin Especificar", np.nan, inplace=True)

# Eliminar filas que tengan NaN en cualquier columna
df2015 = df2015.dropna()

# Mostrar las primeras filas del DataFrame limpio para verificar
print(df2015.head())

import pandas as pd
import numpy as np

# Reemplazar "sin especificar" con NaN
df2016.replace("Sin Especificar", np.nan, inplace=True)

# Eliminar filas que tengan NaN en cualquier columna
df2016 = df2016.dropna()

import pandas as pd
import numpy as np

# Reemplazar "sin especificar" con NaN
df2017.replace("Sin Especificar", np.nan, inplace=True)

# Eliminar filas que tengan NaN en cualquier columna
df2017 = df2017.dropna()

import pandas as pd
import numpy as np

# Reemplazar "sin especificar" con NaN
df2018.replace("Sin Especificar", np.nan, inplace=True)

# Eliminar filas que tengan NaN en cualquier columna
df2018 = df2018.dropna()

import pandas as pd
import numpy as np

# Reemplazar "sin especificar" con NaN
df2019.replace("Sin Especificar", np.nan, inplace=True)

# Eliminar filas que tengan NaN en cualquier columna
df2019 = df2019.dropna()

import pandas as pd
import numpy as np

# Reemplazar "sin especificar" con NaN
df2021.replace("Sin Especificar", np.nan, inplace=True)

# Eliminar filas que tengan NaN en cualquier columna
df2021 = df2021.dropna()

# Mostrar las primeras filas del DataFrame limpio para verificar
print(df2021.head())

import pandas as pd
import numpy as np

# Reemplazar "sin especificar" con NaN
df2022.replace("Sin Especificar", np.nan, inplace=True)

# Eliminar filas que tengan NaN en cualquier columna
df2022 = df2022.dropna()

import pandas as pd
import numpy as np

# Reemplazar "sin especificar" con NaN
df2023.replace("Sin Especificar", np.nan, inplace=True)

# Eliminar filas que tengan NaN en cualquier columna
df2023 = df2023.dropna()

import pandas as pd
import numpy as np

# Reemplazar "sin especificar" con NaN
df2024.replace("Sin Especificar", np.nan, inplace=True)

# Eliminar filas que tengan NaN en cualquier columna
df2024 = df2024.dropna()

import pandas as pd

# Tomar una muestra aleatoria del 20% de los datos
muestra_df2014 = df2014.sample(frac=0.4, random_state=1)
muestra_df2015 = df2015.sample(frac=0.4, random_state=1)
muestra_df2016 = df2016.sample(frac=0.4, random_state=1)
muestra_df2017 = df2017.sample(frac=0.4, random_state=1)
muestra_df2018 = df2018.sample(frac=0.4, random_state=1)
muestra_df2019 = df2019.sample(frac=0.4, random_state=1)
muestra_df2021 = df2021.sample(frac=0.4, random_state=1)
muestra_df2022 = df2022.sample(frac=0.4, random_state=1)
muestra_df2023 = df2023.sample(frac=0.4, random_state=1)
muestra_df2024 = df2024.sample(frac=0.4, random_state=1)

import pandas as pd

# Lista de DataFrames para cada año
dataframes = [
    muestra_df2014, muestra_df2015, muestra_df2016, muestra_df2017, muestra_df2018, muestra_df2019,
    muestra_df2021, muestra_df2022, muestra_df2023, muestra_df2024
]

# Unir todos los DataFrames en uno solo
df_completo = pd.concat(dataframes, ignore_index=True)

# Mostrar las primeras filas del DataFrame unido para verificar
print(df_completo.head())

df_completo.shape

# Filtrar solo las filas donde 'departamento_hospedaje' sea 'Antioquia'
ciudades_antioquia = df_completo[df_completo['departamento_hospedaje'].str.lower() == 'antioquia']

# Obtener los valores únicos de 'ciudad_hospedaje' en el departamento de Antioquia
valores_ciudad_hospedaje = ciudades_antioquia['ciudad_hospedaje'].unique()

# Mostrar los valores únicos
print(valores_ciudad_hospedaje)

# Define las listas de ciudades y países que vamos a filtrar
ciudades_area_metropolitana = [
    'Medellín', 'Itagüí', 'Bello', 'Copacabana', 'La Estrella',
    'Caldas', 'Barbosa', 'Sabaneta', 'Girardota', 'Envigado', 'Itagui'
]
paises_excluidos = ['Colombia', 'Venezuela']




# Muestra las primeras filas del DataFrame filtrado para verificar
print(df_completo.head())

# Filtrar solo las filas donde 'entrada_salida' sea 'Entradas'
df_entradas = df_completo[df_completo['entrada_salida'] == 'Entradas']

# Mostrar las primeras filas del DataFrame filtrado para verificar
print(df_entradas.head())

# Filtrar solo las filas donde 'ciudad_hospedaje' esté en el área metropolitana
df_filtrado = df_completo[df_completo['ciudad_hospedaje'].isin(ciudades_area_metropolitana)]

departamentos_excluidos = ['Boyacá', 'Risaralda', 'Santander']

# Filtrar solo las filas donde 'ciudad_hospedaje' esté en el área metropolitana
df_filtrado = df_completo[df_completo['departamento_hospedaje'].isin(ciudades_area_metropolitana)]

df_filtrado

# Filtrar para excluir 'colombia' y 'venezuela' en 'pais_nacionalidad' y 'pais_procedencia'
df_filtrado1 = df_filtrado[
    ~df_completo['pais_nacionalidad'].isin(paises_excluidos) &
    ~df_completo['pais_destino_procedencia'].isin(paises_excluidos) &
    ~df_completo['departamento_hospedaje'].isin(departamentos_excluidos)
]

df_filtrado1

pip install unidecode

import pandas as pd
import unicodedata

def quitar_tildes(s):
    return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))

# Aplicar la función a la columna 'pais_procedencia' y convertir a minúsculas
df_filtrado1['pais_nacionalidad'] = df_filtrado1['pais_nacionalidad'].apply(quitar_tildes).str.lower()

df_filtrado1

# Exportar a un archivo CSV
# Exportar a un archivo CSV en la carpeta de descargas
df_filtrado1.to_csv('df_filtrado.csv', index=False)

df_filtrado1['tipo_transporte'].unique()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Mapeo de los meses en texto a números
meses = {
    'Enero': 1, 'Febrero': 2, 'Marzo': 3, 'Abril': 4, 'Mayo': 5, 'Junio': 6,
    'Julio': 7, 'Agosto': 8, 'Septiembre': 9, 'Octubre': 10, 'Noviembre': 11, 'Diciembre': 12
}

# Asumiendo que 'df' es tu DataFrame y 'agnio' es el año y 'meses' el mes en formato texto
df['mes_numerico'] = df['meses'].map(meses)

# Crear la columna de fecha combinando año y mes numérico
df['fecha'] = pd.to_datetime(df['agnio'].astype(str) + '-' + df['mes_numerico'].astype(str), format='%Y-%m')

# Agrupar por la nueva columna 'fecha' y contar las visitas
visitas_por_fecha = df.groupby('fecha').size()

# Extraer solo el mes para el eje X
meses_str = visitas_por_fecha.index.month_name()

# Crear el gráfico de serie temporal
plt.figure(figsize=(14, 6))
sns.lineplot(x=meses_str, y=visitas_por_fecha.values, marker='o', color='b')
plt.title("Frecuencia de Visitas por Mes (Serie de Tiempo)")
plt.xlabel("Mes")
plt.ylabel("Cantidad de Visitas")
plt.xticks(rotation=45)
plt.grid()
plt.show()

from statsmodels.tsa.seasonal import seasonal_decompose

# Descomponer la serie de tiempo
descomposicion = seasonal_decompose(visitas_por_fecha, model='additive', period=6)
descomposicion.plot()
plt.show()

"""Se puede observar que la frecuencia de visita se asemeja a las festividades importantes de la ciudad como la feria de flores y los alumbrados navideños, esto nos lleva a reflexionar. Ya que si seguimos incentivando eventos importantes en la ciudad se puede seguir fomentando las visitas."""

import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Asegúrate de que tus datos 'visitas_por_fecha' tienen una frecuencia temporal definida
# Esto es un ejemplo, usa el índice real de tu conjunto de datos
visitas_por_fecha.index = pd.to_datetime(visitas_por_fecha.index)
visitas_por_fecha = visitas_por_fecha.asfreq('MS')  # 'MS' para frecuencia mensual de inicio de mes

# Ajustar el modelo SARIMA
model = SARIMAX(visitas_por_fecha, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))  # Ejemplo
model_fit = model.fit()

# Hacer predicciones
predicciones = model_fit.forecast(steps=12)

# Crear un índice de fechas para las predicciones (semanas o meses según la frecuencia)
fecha_inicio = visitas_por_fecha.index[-1]  # Última fecha en el conjunto de entrenamiento
fechas_prediccion = pd.date_range(fecha_inicio, periods=13, freq='MS')[1:]  # Generar las siguientes 12 fechas (sin la última)

# Graficar los resultados
plt.figure(figsize=(10, 6))

# Graficar las visitas originales
plt.plot(visitas_por_fecha, label='Visitas Originales', color='blue')

# Graficar las predicciones
plt.plot(fechas_prediccion, predicciones, label='Predicciones', color='red', linestyle='--')

# Personalizar el gráfico
plt.title('Predicciones de Visitas (SARIMA)')
plt.xlabel('Mes')
plt.ylabel('Visitas')
plt.legend()

# Mostrar el gráfico
plt.xticks(rotation=45)
plt.grid(True)
plt.show()