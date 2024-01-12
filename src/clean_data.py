import re
import pandas as pd
import numpy as np
from datetime import datetime

def verify_excel(information):
    # Verificar si la columna 'NOMBRE' contiene solo letras y/o espacios (tratando NaN como False)
    information['EsFormatoCorrectoNombre'] = information['NOMBRE'].apply(lambda x: bool(re.match('^[a-zA-Z ]+$', str(x))) if not pd.isna(x) else False)

    # Verificar si la columna 'APELLIDO' contiene solo letras y/o espacios (tratando NaN como False)
    information['EsFormatoCorrectoApellido'] = information['APELLIDO'].apply(lambda x: bool(re.match('^[a-zA-Z ]+$', str(x))) if not pd.isna(x) else False)

    # Verificar si la columna 'NUMERO' contiene exactamente 10 dígitos (tratando NaN como False)
    information['EsFormatoCorrectoNumero'] = information['NUMERO'].apply(lambda x: bool(re.match('^\d{10}$', str(x))) if not pd.isna(x) else False)

    # Verificar si la columna 'ULTIMO_PAGO' contiene el formato dd/MM/AAAA y si es menor o igual a la fecha actual
    current_date = datetime.now().strftime('%d/%m/%Y')
    information['EsFormatoCorrectoUltimoPago'] = information['ULTIMO_PAGO'].apply(lambda x: 
        bool(re.match('^\d{2}/\d{2}/\d{4}$', str(x))) and datetime.strptime(str(x), '%d/%m/%Y') <= datetime.now()
        if not pd.isna(x) else False
    )
    # Filtrar solo las filas donde todas las columnas 'EsFormatoCorrecto' son True
    df_formato_correcto = information[
        (information['EsFormatoCorrectoNombre']) &
        (information['EsFormatoCorrectoApellido']) &
        (information['EsFormatoCorrectoNumero']) &
        (information['EsFormatoCorrectoUltimoPago'])
    ].copy()  # Usamos copy() para evitar problemas de referencia al DataFrame original

    # Filtrar solo las filas donde al menos una columna 'EsFormatoCorrecto' es False
    df_formato_incorrecto = information[
        ~((information['EsFormatoCorrectoNombre']) &
        (information['EsFormatoCorrectoApellido']) &
        (information['EsFormatoCorrectoNumero']) &
        (information['EsFormatoCorrectoUltimoPago']))
    ].copy()  # Usamos copy() para evitar problemas de referencia al DataFrame original

    # Eliminar las columnas de verificación en ambos DataFrames
    df_formato_correcto = df_formato_correcto.drop(columns=['EsFormatoCorrectoNombre', 'EsFormatoCorrectoApellido', 'EsFormatoCorrectoNumero', 'EsFormatoCorrectoUltimoPago'])
    df_formato_incorrecto = df_formato_incorrecto.drop(columns=['EsFormatoCorrectoNombre', 'EsFormatoCorrectoApellido', 'EsFormatoCorrectoNumero', 'EsFormatoCorrectoUltimoPago'])

    return df_formato_correcto, df_formato_incorrecto
