import os
import pywhatkit as kit
from datetime import datetime

try:
    diccionario_deudores = {
        "Jacobo Montenegro Angel": "3233073789",
        "Juan Jose Gomez": "3165326067",
        "Daniel Carvajal Correa": "3193917279",
        "Manuela Correa Lopez": "3185957386"
    }

    for nombre, numero in diccionario_deudores.items():
        # Agrega el código de marcación para Colombia y Strip quita los espacios en blanco
        numero_colombia = "+57" + numero.strip()

        # Join se utiliza para concatenar cadenas y las separa
        ruta_directorio = os.path.join('c:\\villa_fc\\directorio', f'{nombre}_{numero}')
        
        # makedirs crea directorios
        # Si exist_ok=True, la función no generará un error si el directorio ya existe
        os.makedirs(ruta_directorio, exist_ok=True)

        mensaje = f'Hola {nombre}.\n\n🚩Recuerda tu cuota pendiente en Villa_FC.\n\nPor favor, realiza el pago pronto para evitar inconvenientes. ¡Gracias!'
        hora_envio = datetime.now().hour
        minuto_envio = datetime.now().minute + 1

        # Corrige la función de envío de mensajes
        kit.sendwhatmsg_instantly(numero_colombia, mensaje, hora_envio, minuto_envio)

        print(f"Diccionario creado: {ruta_directorio}, mensaje enviado a {nombre} al número {numero_colombia}")

except Exception as e:
    print(f"Ha ocurrido un error: {str(e)}")