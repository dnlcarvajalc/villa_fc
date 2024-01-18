import pandas as pd
import os
import constants

def concatenar_archivos_excel():
    """Esta función concatena varios archivos de excel para unificar información
      y posteriormente genera un arhicvo y un dataframe con la información

    Returns:
        united_data: un dataframe que contiene los archivos unificados
    """
    #Archivos que se van a concatenar
    archivos_excel = os.listdir('./data')

    #Este dataframe vacio es donde se va a almacenar la info concatenada
    united_data = pd.DataFrame()

    #Recorre cada uno de los archivos para posteriormente leerlos en el dataframe
    for archivo in archivos_excel:
        df = pd.read_excel('./data/' + archivo)
        #Concateno todos los archivos los archivos
        united_data = pd.concat([united_data,df], ignore_index=True)

    if 'ULTIMO_PAGO' in united_data.columns:
        #Formato columna FECHA dd/mm/aa y sin hora
        united_data['ULTIMO_PAGO']= united_data['ULTIMO_PAGO'].dt.strftime(constants.DATE_FORMAT)

    #Agrega la información en un archivo
    united_data.to_excel("./final_data/Final_date.xlsx", index=False)

    return united_data
