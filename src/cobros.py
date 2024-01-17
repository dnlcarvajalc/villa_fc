import pandas as pd
import constants
from datetime import datetime

def conv_datetime (df):
    """Esta Funcion convierte las fechas del df en tipo datetime

    Args:
        df (pd.Dataframe): Data frame con toda la informacion de pagos

    Returns:
        pd.Dataframe: Data frame con la fecha en formato año, mes, dia 
    """
    df_new = pd.to_datetime(df['ULTIMO_PAGO'], format= constants.DATE_FORMAT)
    return df_new


def diccionario_deudores (df_new):
    """Funcion para crear un diccionario en el cual se guarden las personas cuyo ultimo 
       pago sea superior a 30 dias  

    Args:
        df_new (pd.Dataframe): data frame con la fecha convertida al formato año, mes, dia
    """
    deudores = {}
    for index, cliente in df_new.iterrows():
        fecha_convertida = conv_datetime(cliente)
        fecha = datetime.now()
        df_new.at[index, 'Diferencia'] = fecha_convertida - fecha
        if df_new.at[index, 'Diferencia'] < constants.LIMIT_DAYS:        
            deudores.update({cliente['NOMBRE']: cliente['NUMERO']})
    print(df_new) 
    print(deudores)