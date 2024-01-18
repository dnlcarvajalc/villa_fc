import pywhatkit as kit
from datetime import datetime

def enviar_mensajes(diccionario_deudores:dict):

    """ Esta función automatiza el envío de mensajes de recordatorio
        a los deudores a través de WhatsApp, recordandoles sobre sus
        cuotas pendientes a Villa_Fc, utilizando un diccionario
        con la información de los deudores.

    Args:
        diccionario_deudores (dict):
        Este diccionario almacena la información (Nombre y Número) de los deudores
        y se proporciona como argumentos.
    """

    try:

        for nombre, numero in diccionario_deudores.items():
            # Agrega el código de marcación para Colombia y Strip quita los espacios en blanco del número
            numero_colombia = "+57" + str(numero).strip()

            mensaje = f'Hola {nombre}.\n\n🚩Recuerda tu cuota pendiente en Villa_FC.\n\nPor favor, realiza el pago pronto para evitar inconvenientes. ¡Gracias!'
            hora_envio = datetime.now().hour
            minuto_envio = datetime.now().minute + 1

            # Envío de mensajes a WhatsApp
            kit.sendwhatmsg_instantly(numero_colombia, mensaje, hora_envio, minuto_envio)

            print(f"Mensaje enviado a {nombre} al número {numero_colombia}")

    except Exception as e:
        print(f"Ha ocurrido un error: {str(e)}")
