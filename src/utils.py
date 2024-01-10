import pandas as pd

def read_excel(file_path:str):
    df = pd.read_excel(file_path)
    print(df)
    return df

