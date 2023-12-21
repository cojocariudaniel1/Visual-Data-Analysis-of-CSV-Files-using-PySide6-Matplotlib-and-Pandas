import pandas as pd


def get_data():
    file_name = "baza_de_date1.xls"
    sheet = "superstore"
    df = pd.read_excel(io=file_name, sheet_name=sheet, usecols="A:U")

    return df

def get_data_with_state_id():
    file_name = "baza_de_date_cu_state_id.xlsx"
    sheet = "sheet"
    df = pd.read_excel(io=file_name, sheet_name=sheet)
    return df

def get_usa_data():
    file_name = "uszips.xlsx"
    sheet = "sheet"
    df = pd.read_excel(io=file_name, sheet_name=sheet)
    return df


def add_state_codes(dataframe_superstore, dataframe_city):
    # Găsește cel mai frecvent state_id pentru fiecare oraș
    most_frequent_state = dataframe_city.groupby("City")[["state_id", "lat", "lng", "zip"]].agg(
        lambda x: x.value_counts().idxmax()).reset_index()
    # print(most_frequent_state.to_string(index=False))
    # Adaugă state_id în dataframe_superstore pe baza celor mai frecvente asocieri
    dataframe_superstore = pd.merge(dataframe_superstore, most_frequent_state, how="left", left_on="City",
                                    right_on="City")

    return dataframe_superstore


def get_big_df():
    us_dataframe = get_usa_data()
    df = get_data()
    dfx = add_state_codes(df, us_dataframe).dropna()
    dfx.to_excel('baza_de_date_cu_state_id.xlsx', index=False)  # Specificați numele dorit pentru fișier
    return dfx



