import pandas as pd


#Archivos que se van a concatenar
archivos_excel = {'./data/villa_fc.xlsx','./data/fake_list.xlsx'}

#Este dataframe vacio es donde se va a almacenar la info concatenada
united_data = pd.DataFrame()

#Recorre cada uno de los archivos para posteriormente leerlos en el dataframe
for archivos in archivos_excel:
    df = pd.read_excel(archivos)
    #print(df)
    
    #Concateno todos los archivos los archivos
    united_data = pd.concat([united_data,df], ignore_index=True)
    #united_data = united_data.append(df,ignore_index=True)

#Agrega la información en un archivo
united_data.to_excel("./final_data/Final_date.xlsx", index=False)