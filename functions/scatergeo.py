import pandas as pd
import plotly.express as px

from functions.basic_functions import get_data

# Datele tale
state_codes = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

def add_state_codes(dataframe):
    # Adaugă o coloană numită "State Code" care conține codurile statelor
    dataframe["State Code"] = dataframe["State"].map(state_codes)
    return dataframe

if __name__ == "__main__":
    # Exemplu de
    dfx = get_data()

    df = add_state_codes(dfx)
    # Adaugă coloana cu codurile statelor
    result_df = df.groupby(["State Code","City" , pd.to_datetime(df["Order Date"]).dt.to_period("M")])["Sales"].sum().reset_index()

    fig = px.choropleth(result_df, locations='State Code', color='Sales', hover_name='State Code', locationmode='USA-states',
                        title='GDP per Capita by Country',animation_group= "State Code", animation_frame="Order Date", scope="usa")
    fig.show()
