import pandas as pd


def get_data():
    file_name = "baza_de_date.xls"
    sheet = "superstore"
    df = pd.read_excel(io=file_name, sheet_name=sheet, usecols="A:U")

    dataframe = pd.DataFrame(df)
    return dataframe


def get_City():
    dataframe = get_data()
    all_cities = dataframe["City"].drop_duplicates().tolist()
    return all_cities


def get_Category():
    dataframe = get_data()
    all_Category = dataframe["Category"].drop_duplicates().tolist()
    return all_Category


def get_State():
    dataframe = get_data()
    all_states = dataframe["State"].drop_duplicates().tolist()
    return all_states


def get_subCategory():
    dateframe = get_data()
    all_sub_category = dateframe["Sub-Category"].drop_duplicates().tolist()
    return all_sub_category


def get_Segment():
    dateframe = get_data()
    segment = dateframe["Segment"].drop_duplicates().tolist()
    return segment


def get_ShipMode():
    dateframe = get_data()
    shipmode = dateframe["Ship Mode"].drop_duplicates().tolist()
    return shipmode
