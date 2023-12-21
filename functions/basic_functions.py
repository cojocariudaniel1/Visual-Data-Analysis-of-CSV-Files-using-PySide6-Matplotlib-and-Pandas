import pandas as pd


def get_data():
    file_name = "baza_de_date1.xls"
    sheet = "superstore"
    df = pd.read_excel(io=file_name, sheet_name=sheet, usecols="A:U")

    dataframe = pd.DataFrame(df)
    print(dataframe.columns)
    return dataframe


def get_City():
    dataframe = get_data()
    all_cities = dataframe["City"].drop_duplicates().tolist()
    return all_cities


def get_Category():
    dataframe = get_data()
    all_Category = dataframe["Category"].drop_duplicates().tolist()
    print(all_Category)
    return all_Category

def get_State():
    dataframe = get_data()
    all_State = dataframe["State"].drop_duplicates().tolist()
    return all_State

def get_Segment():
    dataframe = get_data()
    all_segment = dataframe["Segmet"].drop_duplicates().tolist()
    return all_segment

def get_subCategory():
    dataframe = get_data()
    subcategory = dataframe["Sub-Category"].drop_duplicates().tolist()
    return subcategory


def get_ShipMode():
    dataframe = get_data()
    ship_mode = dataframe["Ship Mode"].drop_duplicates().tolist()
    return ship_mode