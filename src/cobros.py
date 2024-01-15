import pandas as pd
import constants
from datetime import datetime


fecha = datetime.now()


def conv_datetime (df):
    df_new = pd.to_datetime(df['ULTIMO_PAGO'], format= constants.DATE_FORMAT)
    return df_new

def diccionario_deudores (df_new):
    deudores = {}
    for index, cliente in df_new.iterrows():
        fecha_convertida = conv_datetime(cliente)
        df_new.at[index, 'Diferencia'] = fecha_convertida - fecha
        if df_new.at[index, 'Diferencia'] < constants.LIMIT_DAYS:        
            deudores.update({cliente['NOMBRE']: cliente['NUMERO']})
     

