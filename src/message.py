import pandas as pd
import os
import pywhatkit as kit       # Biblioteca para enviar mensajes a whatsapp
from datetime import datetime # Módulo para manipular fechas y horas

directorio = 'C:\\Users\\mcorr\\OneDrive\\Documentos\\ESTUDIO_PROGRAMACIÓN\\Proyecto_1\\villa_fc\\ensayo.xlsx'
df = pd.read_excel(directorio)

columna_nombres = 'NOMBRE'
columna_numeros = 'NUMERO'

# iterrows: Permite iterar sobre las filas de un DataFrame, 
# devolviendo para cada iteración un índice y una Serie que 
# contiene los datos de esa fila.

for index, fila in df.iterrows():
    nombre = fila[columna_nombres]
    numero = str(fila[columna_numeros])

# Agrega el código de marcación para Colombia y Strip quita los espacios en blanco
    numero_colombia = "+57" + numero.strip()
    
# Join se utiliza para concatenar cadenas y las separa
    ruta_directorio = os.path.join('C:\\Users\\mcorr\\OneDrive\\Documentos\\ESTUDIO_PROGRAMACIÓN\\Proyecto_1\\villa_fc\\directorio', f'{nombre}_{numero}')
# makedirs crea directorios
# Si exist_ok=True, la función no generará un error si el directorio ya existe
    os.makedirs(ruta_directorio, exist_ok=True)
        
    mensaje = f'Hola {nombre}, esto es una prueba'
    hora_envio = datetime.now().hour
    minuto_envio = datetime.now().minute + 1

    # Corrige la función de envío de mensajes
    kit.sendwhatmsg_instantly(numero_colombia, mensaje, hora_envio, minuto_envio)

    print(f"Directorio creado: {ruta_directorio}, mensaje enviado a {nombre} al número {numero_colombia}")
