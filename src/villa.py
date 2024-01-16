import constants
import utils
import clean_data

if __name__ == "__main__":
    df = utils.read_excel(constants.EXCEL_PATH)

    df_clean_correct = clean_data.verify_excel(df)


