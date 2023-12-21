import logging

import folium as fol
import pandas as pd
from folium import folium


def get_data():
    file_name = "baza_de_date_cu_state_id.xlsx"  # path to file + file name
    sheet = "sheet"  # sheet name or sheet number or list of sheet numbers and names
    df = pd.read_excel(io=file_name, sheet_name=sheet, usecols="A:U")

    dataframe = pd.DataFrame(df)
    return dataframe


central = [43.934461082838965, -96.22057172688287]
west = [42.07819545813198, -115.88890149175025]
south = [31.819477866201037, -99.097218661424]
east = [42.07626767970349, -76.30252620306574]


def mean_sales():
    df = get_data()

    dataframe = df[["Sales", "Category"]]

    # Face suma la vanzari (TOTAL)
    df2 = dataframe.sum(numeric_only=True)
    total = int(df2)

    df1 = dataframe.groupby("Category").sum(numeric_only=True).reset_index()

    list_df1 = []

    for i in range(len(df1)):
        list_df1.append([df1.iloc[i][0], (df1.iloc[i][1] / total) * 100])
    return list_df1


def get_info(region):
    try:
        df = get_data()

        dataframe = df[["Region", "Sales", "Category"]]
        #
        df2 = dataframe[dataframe["Region"] == region].sum()
        total = df2[1]
        #
        df1 = dataframe[dataframe["Region"] == region].groupby("Category").sum(numeric_only=True).reset_index()
        list_df1 = []
        for i in range(len(df1)):
            list_df1.append([df1.iloc[i][0], (df1.iloc[i][1] / total) * 100])
        return list_df1

    except BaseException as e:
        logging.exception(e)



def zona(regiune):
    if regiune == "Central":
        map = folium.Map(location=central,
                         zoom_start=5.3, control_scale=True)
        marker(map, get_info("Central"), central)
        fol.Marker(
            central, popup="<i>Central</i>", tooltip="Central",
        ).add_to(map)

        return map
    elif regiune == "South":
        map = folium.Map(location=south,
                         zoom_start=5.3, control_scale=True)
        marker(map, get_info("South"), south)
        fol.Marker(
            south, popup="<i>South</i>", tooltip='South'
        ).add_to(map)

        return map
    elif regiune == "East":
        map = folium.Map(location=east,
                         zoom_start=5.3, control_scale=True)
        marker(map, get_info("East"), east)
        fol.Marker(
            east, popup="<i>East</i>", tooltip="East"
        ).add_to(map)

        return map
    elif regiune == "West":
        map = folium.Map(location=west,
                         zoom_start=5.3, control_scale=True)
        marker(map, get_info("West"), west)
        fol.Marker(
            west, popup="<i>West</i>", tooltip='West'
        ).add_to(map)

        return map


def map_create():
    try:
        regions = ["South", "East", "Central", "West"]
        map = folium.Map(location=[40.195267148677914, -101.46781948956031],
                         zoom_start=4.4, control_scale=True)

        for i in regions:
            if i == "South":
                marker(map, get_info(i), south)
            elif i == "West":
                marker(map, get_info(i), west)
            elif i == "Central":
                marker(map, get_info(i), central)
            elif i == "East":
                marker(map, get_info(i), east)

        fol.Marker(
            central, popup="<i>Central</i>", tooltip="Central",
        ).add_to(map)

        fol.Marker(
            east, popup="<i>East</i>", tooltip="East"
        ).add_to(map)

        fol.Marker(
            south, popup="<i>South</i>", tooltip='South'
        ).add_to(map)

        fol.Marker(
            west, popup="<i>West</i>", tooltip='West'
        ).add_to(map)

        return map
    except BaseException as e:
        logging.exception(e)


def marker(map, data, zone):
    try:
        count = 0
        list1 = []
        for i in data:
            value = f"{i[1]:.2f} %"
            string = f"{str(i[0]) + '   ' + str(value)}"
            list1.append(string)
        fol.Marker(
            [zone[0] + count, zone[1] + 1],
            icon=fol.DivIcon(html=f"""<div style="font-family: Verdana, sans-serif; width: 300px; color: blue; 
            font-weight:bold;font-size: 13px;
            box-sizing: border-box;
              width: 190px;
              height: 65px;
              border: 2px solid #969696;
              background: #FFFFFF;
              opacity: 0.7;
              margin: 2px; ">{', '.join(list1)}</div>""")).add_to(map)
        count += 2
    except BaseException as e:
        logging.exception(e)
