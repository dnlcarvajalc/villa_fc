import constants
import utils
import United_Data
from message import enviar_mensajes

diccionario_deudores = {
            "Jacobo Montenegro Angel": "3233073789",
            "Juan Jose Gomez": "3165326067",
            "Daniel Carvajal Correa": "3193917279",
            "Manuela Correa Lopez": "3185957386"
        }

if __name__ == "__main__":
    #Llama la función concatenar archivos excel
    United_Data.concatenar_archivos_excel()

    df = utils.read_excel(constants.EXCEL_PATH)

    #Llama la función       
    #enviar_mensajes(diccionario_deudores)