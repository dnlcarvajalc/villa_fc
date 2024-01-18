import re
import pandas as pd
import numpy as np
from datetime import datetime

def verify_excel(information):
    # Verificar si la columna 'NOMBRE' contiene solo letras y/o espacios (tratando NaN como False)
    information['CorrectName'] = information['NOMBRE'].apply(lambda x: bool(re.match('^[a-zA-ZñÑáéíóúÁÉÍÓÚ ]+$', str(x))) if not pd.isna(x) else False)

    # Verificar si la columna 'APELLIDO' contiene solo letras y/o espacios (tratando NaN como False)
    information['CorrectLastName'] = information['APELLIDO'].apply(lambda x: bool(re.match('^[a-zA-ZñÑáéíóúÁÉÍÓÚ ]+$', str(x))) if not pd.isna(x) else False)

    # Verificar si la columna 'NUMERO' contiene exactamente 10 dígitos (tratando NaN como False)
    information['CorrectNumberPhone'] = information['NUMERO'].apply(lambda x: bool(re.match('^\d{10}$', str(x))) if not pd.isna(x) else False)

    # Verificar si la columna 'ULTIMO_PAGO' contiene el formato dd/MM/AAAA y si es menor o igual a la fecha actual (tratando NaN como False)
    information['CorrectDate'] = information['ULTIMO_PAGO'].apply(lambda x: 
        bool(re.match('^\d{2}/\d{2}/\d{4}$', str(x))) and datetime.strptime(str(x), '%d/%m/%Y') <= datetime.now()
        if not pd.isna(x) else False
    )
    # Filtrar solo las filas donde todas las columnas 'EsFormatoCorrecto' son True
    df_formato_correcto = information[
        (information['CorrectName']) &
        (information['CorrectLastName']) &
        (information['CorrectNumberPhone']) &
        (information['CorrectDate'])
    ].copy()  # Usamos copy() para evitar problemas de referencia al DataFrame original

    # Filtrar solo las filas donde al menos una columna 'EsFormatoCorrecto' es False
    df_formato_incorrecto = information[
        ~((information['CorrectName']) &
        (information['CorrectLastName']) &
        (information['CorrectNumberPhone']) &
        (information['CorrectDate']))
    ].copy()  # Usamos copy() para evitar problemas de referencia al DataFrame original

    # Eliminar las columnas de verificación en ambos DataFrames
    df_formato_correcto = df_formato_correcto.drop(columns=['CorrectName', 'CorrectLastName', 'CorrectNumberPhone', 'CorrectDate'])
    df_formato_incorrecto_false = df_formato_incorrecto.drop(columns=['NOMBRE', 'APELLIDO', 'NUMERO', 'ULTIMO_PAGO'])
    df_formato_incorrecto = df_formato_incorrecto.drop(columns=['CorrectName', 'CorrectLastName', 'CorrectNumberPhone', 'CorrectDate'])
    
    filas = len(df_formato_incorrecto_false)

    if filas > 0:            
        print("\n Información incorrecta")
        print(df_formato_incorrecto)
        print("\n") 
        for index, row in df_formato_incorrecto_false.iterrows():
            if row['CorrectName'] == False:
                print(f"En la columna 'NOMBRE' hay un error en la fila {index + 1}")
            if row['CorrectLastName'] == False:
                print(f"En la columna 'APELLIDO' hay un error en la fila {index + 1}")
            if row['CorrectNumberPhone'] == False:
                print(f"En la columna 'NUMERO' hay un error en la fila {index + 1}")
            if row['CorrectDate'] == False:
                print(f"En la columna 'ULTIMO_PAGO' hay un error en la fila {index + 1}")
    else:
        print("Información correcta")

    return df_formato_correcto
