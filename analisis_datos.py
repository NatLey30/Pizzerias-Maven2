import pandas as pd


def archivo(fichero, file, df):
    '''
    Función que va a analizar cada archivo buscando cuantos
    Nans y Nulls hay en todo el csv. También va a estudiar la
    tipología de cada columna, a la vaz que mira cuantos
    Nans y Nulls hay en esta.
    '''
    file.write(f'ANALISIS DE DATOS DEL FICHERO {fichero}\n')

    # Nans totales
    nans = str(df.isna().sum().sum())
    file.write(f'Nans totales: {nans}\n')

    # Nulls totales
    nulls = str(df.isnull().sum().sum())
    file.write(f'Nans totales: {nulls}\n')

    # Sacamos columnas
    columnas = df.columns.values

    # Para cada columna
    for colum in range(len(columnas)):
        nombre = columnas[colum]
        file.write(f'   La columna es: "{nombre}"\n')

        # Buscamos su tipología
        tipo_col = str(df[columnas[colum]].dtype)
        file.write(f'       La columna del tipo: {tipo_col}\n')

        # Número de nans
        nans_col = str(df[columnas[colum]].isna().sum().sum())
        file.write(f'       Los Nans de la columna son: {nans_col}\n')

        # Número de nulls
        nulls_col = str(df[columnas[colum]].isnull().sum().sum())
        file.write(f'       Los Nans de la columna son: {nulls_col}\n')


if __name__ == "__main__":

    # Abrimos el fichero donde guardamos el analisis
    file = open("analisis_archivos.txt", 'w')

    # Analizamos cada archivo
    df = pd.read_csv('order_details.csv', sep=';', encoding='LATIN1')
    archivo('order_details.csv', file, df)
    file.write('\n')
    df = pd.read_csv('orders.csv', sep=';', encoding='LATIN1')
    archivo('orders.csv', file, df)
    file.write('\n')
    df = pd.read_csv('data_dictionary.csv', sep=',', encoding='LATIN1')
    archivo('data_dictionary.csv', file, df)
    file.write('\n')
    df = pd.read_csv('pizzas.csv', sep=',', encoding='LATIN1')
    archivo('pizzas.csv', file, df)
    file.write('\n')
    df = pd.read_csv('pizza_types.csv', sep=',', encoding='LATIN1')
    archivo('pizza_types.csv', file, df)

    # Cerramos archivo
    file.close()
