import constants
import utils
import clean_data

if __name__ == "__main__":
    df = utils.read_excel(constants.EXCEL_PATH)

    df_clean_correct, df_clean_incorrect = clean_data.verify_excel(df)

# if df_clean_incorrect.empty:
    print("\nLa informacion tiene algún error en los siguientes registros: ") 
    print(df_clean_incorrect)
