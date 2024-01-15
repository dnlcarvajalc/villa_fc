import constants
import utils
import cobros
import pandas as pd


if __name__ == "__main__":
    df = utils.read_excel(constants.EXCEL_PATH)    
    cobros.diccionario_deudores(df) 