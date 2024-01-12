import pywhatkit as kit
from datetime import datetime

def enviar_mensajes(diccionario_deudores):

    try:
        
        for nombre, numero in diccionario_deudores.items():
            # Agrega el código de marcación para Colombia y Strip quita los espacios en blanco del número
            numero_colombia = "+57" + numero.strip()

            mensaje = f'Hola {nombre}.\n\n🚩Recuerda tu cuota pendiente en Villa_FC.\n\nPor favor, realiza el pago pronto para evitar inconvenientes. ¡Gracias!'
            hora_envio = datetime.now().hour
            minuto_envio = datetime.now().minute + 1

            # Envío de mensajes a WhatsApp
            kit.sendwhatmsg_instantly(numero_colombia, mensaje, hora_envio, minuto_envio)

            print(f"Mensaje enviado a {nombre} al número {numero_colombia}")

    except Exception as e:
        print(f"Ha ocurrido un error: {str(e)}")
