import pandas as pd

def read_excel(file_path:str):
    """Funcion encargada de leer los datos del archivo excel almacenado.

    Args:
        file_path (str): la ruta del archivo excel

    Returns:
        pd.DataFrame: El dataframe completo con la informacion
    """
    df = pd.read_excel(file_path)
    return df