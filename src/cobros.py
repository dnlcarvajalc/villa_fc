import pandas as pd
import constants
from datetime import datetime


fecha = datetime.now()
print(fecha)


def obtenerColumna (df):
     columnaD = df.iloc[:, constants.COLUM_NUMBER]
     return columnaD

def conv_datetime (df):
    df_new = pd.to_datetime(df['ULTIMO_PAGO'], format='%d/%m/%Y')
    print("holi")
    print(df_new)
    return df_new

def resta_fechas (df_new):
    df_new['Diferencia'] = None
    deudores = {}
    for index, cliente in df_new.iterrows():
    # Realizar la resta y asignar el resultado a la columna 'Diferencia'
        fecha_convertoda = conv_datetime(cliente)
        df_new.at[index, 'Diferencia'] = fecha_convertoda - fecha
        if df_new.at[index, 'Diferencia'] < constants.LIMIT_DAYS:        
            deudores.update({cliente['NOMBRE']: cliente['NUMERO']})
    print(df_new)
    print(deudores)
    

