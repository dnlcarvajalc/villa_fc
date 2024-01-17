import pandas as pd
import os
import constants

#Archivos que se van a concatenar
#archivos_excel = {'./data/villa_fc.xlsx','./data/fake_list.xlsx'}
archivos_excel = os.listdir('./data')

#Este dataframe vacio es donde se va a almacenar la info concatenada
united_data = pd.DataFrame()

#Recorre cada uno de los archivos para posteriormente leerlos en el dataframe
for archivos in archivos_excel:
    df = pd.read_excel('./data/' + archivos_excel[1])
    #print(df)
    
    #Concateno todos los archivos los archivos
    united_data = pd.concat([united_data,df], ignore_index=True)
    
if 'ULTIMO_PAGO' in united_data.columns:

    #Formato columna FECHA dd/mm/aa y sin hora
    #united_data['ULTIMO_PAGO']= united_data['ULTIMO_PAGO'].dt.strftime('%d/%m/%Y')
    united_data['ULTIMO_PAGO']= united_data['ULTIMO_PAGO'].dt.strftime(constants.DATE_FORMAT)

#Agrega la información en un archivo
united_data.to_excel("./final_data/Final_date.xlsx", index=False)