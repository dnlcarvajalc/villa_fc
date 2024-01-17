import constants
import utils
import concat_data
import cobros
import pandas as pd
from message import enviar_mensajes

diccionario_deudores = {
            "Jacobo Montenegro Angel": "3233073789",
            "Juan Jose Gomez": "3165326067",
            "Daniel Carvajal Correa": "3193917279",
            "Manuela Correa Lopez": "3185957386"
        }

if __name__ == "__main__":
    #Llama la función concatenar archivos excel
    concat_data.concatenar_archivos_excel()

    df = utils.read_excel(constants.EXCEL_PATH)

    #Llama la función       
    enviar_mensajes(diccionario_deudores)
    cobros.diccionario_deudores(df) 
