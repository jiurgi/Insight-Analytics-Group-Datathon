import pandas as pd

#Función para la limpieza de los datos
def limpieza_datos(data):
    #Copia del dataframe original
    data_copy = data.copy()

    #Eliminamos las columnas que no son de interés
    data_copy = data_copy.drop([0, 1, 2, 3, 4, 5, 6, 7, 8])

    #Reiniciamos los índices y ponemos las columnas como la primera fila
    data_copy = data_copy.reset_index(drop=True)
    data_copy.columns = data_copy.iloc[0]
    data_copy = data_copy.drop([0])
    data_copy = data_copy.reset_index(drop=True)

    return data_copy


#Función para filtrar los datos
def filtrar_datos(data, departamento, municipios):
    #Revisión de los datos de la columna "DEPARTAMENTO" cuyo valor sea igual a "ANTIOQUIA"
    data_antioquia = data[data['DEPARTAMENTO'] == departamento]

    #Revisión de los datos de la columna "DEPARTAMENTO" cuyo valor sea igual a "ANTIOQUIA" y "MUNICIPIO" sea igual a "CALDAS", "LA ESTRELLA", "ITAGUI", "ENVIGADO", "SABANETA",  "MEDELLÍN (CT)", "BELLO", "COPACABANA", "GIRARDOTA" Y "BARBOSA"
    data_municipios = data_antioquia[data_antioquia['MUNICIPIO'].isin(municipios)]

    return data_municipios


#Función para dividir la fecha en año, mes y día
def dividir_fecha(data):
    #Cambio del tipo de dato de la columna "FECHA HECHO" a datetime
    data['FECHA HECHO'] = pd.to_datetime(data['FECHA HECHO'], format='%d/%m/%Y')

    #Separación de la columna "FECHA HECHO" en "AÑO", "MES" y "DÍA"
    data['AÑO'] = data['FECHA HECHO'].dt.year
    data['MES'] = data['FECHA HECHO'].dt.month
    data['DÍA'] = data['FECHA HECHO'].dt.day

    #Eliminación de la columna "FECHA HECHO"
    data = data.drop(columns=['FECHA HECHO'])

    return data


#Función para obtener la serie de tiempo de eventos por municipio
def serie_tiempo(data):
    #Reduzco el dataframe a las columnas "MUNICIPIO", "AÑO", "MES", "DÍA" Y "CANTIDAD"
    timeserie = data[['MUNICIPIO', 'AÑO', 'MES', 'DÍA', 'CANTIDAD']]

    return timeserie