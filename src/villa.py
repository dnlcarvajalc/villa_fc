import concat_data
import cobros
import graficos
from message import enviar_mensajes
import clean_data

if __name__ == "__main__":
    #Llama la función concatenar archivos excel
    df = concat_data.concatenar_archivos_excel()
    df_clean_correct = clean_data.verify_excel(df)
    deudores, acreedores = cobros.diccionario_deudores(df_clean_correct)

    #Llama la función
    enviar_mensajes(deudores)
    graficos.graficar(deudores, acreedores)
