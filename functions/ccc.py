import pandas as pd
import plotly.express as px

from functions.basic_functions import get_data
from functions.dataframeModify import get_big_df, get_data_with_state_id


def grafic_bar_vanzari_pe_an():
    # Datele tale
    dfx = get_data_with_state_id()

    # Adaugă codurile de stare lipsă pentru fiecare lună
    all_states = dfx["state_id"].drop_duplicates().tolist()
    all_dates = pd.date_range(start=dfx["Order Date"].min(), end=dfx["Order Date"].max(), freq='D')

    product = pd.MultiIndex.from_product([all_dates, all_states], names=['Order Date', 'state_id'])
    empty_df = pd.DataFrame(index=product).reset_index()

    # Uneste datele existente cu DataFrame-ul gol pentru a completa toate combinațiile posibile
    df = pd.merge(empty_df, dfx, how='left', on=['Order Date', 'state_id'])

    # Gruparea după an și stat, calcularea sumei vânzărilor și resetarea indexului
    result_df = df.groupby([pd.to_datetime(df["Order Date"]).dt.to_period("Y"), "state_id"])["Sales"].sum().reset_index()

    # Calculați 25% din valoarea maximă a vânzărilor
    mid_point = result_df["Sales"].max() * 0.1

    # Alegeți o hartă de culori distinctă
    color_scale = px.colors.sequential.Inferno_r

    fig = px.bar(result_df,
                 x="state_id",
                 y="Sales",
                 color="Sales",
                 animation_frame="Order Date",
                 animation_group="state_id",
                 color_continuous_scale=color_scale,
                 range_color=[min(result_df["Sales"].tolist()), max(result_df["Sales"].tolist())],
                 range_y=[min(result_df["Sales"].tolist()), max(result_df["Sales"].tolist())],
                 color_continuous_midpoint=mid_point  # Setați midpoint-ul la 25%
                )

    fig.show()

def grafic_bar_vanzari_pe_luna():
    # Datele tale
    dfx = get_data_with_state_id()

    # Adaugă codurile de stare lipsă pentru fiecare lună
    all_states = dfx["state_id"].drop_duplicates().tolist()
    all_dates = pd.date_range(start=dfx["Order Date"].min(), end=dfx["Order Date"].max(), freq='D')

    product = pd.MultiIndex.from_product([all_dates, all_states], names=['Order Date', 'state_id'])
    empty_df = pd.DataFrame(index=product).reset_index()

    # Uneste datele existente cu DataFrame-ul gol pentru a completa toate combinațiile posibile
    df = pd.merge(empty_df, dfx, how='left', on=['Order Date', 'state_id'])

    # Gruparea după lună și stat, calcularea sumei profitului și resetarea indexului
    result_df = df.groupby([pd.to_datetime(df["Order Date"]).dt.to_period("M"), "state_id"])[
        "Sales"].sum().reset_index()

    fig = px.bar(result_df, x="state_id", y="Sales", color="Sales",
      animation_frame="Order Date", animation_group="state_id", range_y=[min(result_df["Sales"].tolist()), max(result_df["Sales"].tolist())])
    fig.show()

def grafic_bar_pe_profit():
    # Datele tale
    dfx = get_data_with_state_id()

    # Adaugă codurile de stare lipsă pentru fiecare lună
    all_states = dfx["state_id"].drop_duplicates().tolist()
    all_dates = pd.date_range(start=dfx["Order Date"].min(), end=dfx["Order Date"].max(), freq='D')

    product = pd.MultiIndex.from_product([all_dates, all_states], names=['Order Date', 'state_id'])
    empty_df = pd.DataFrame(index=product).reset_index()

    # Uneste datele existente cu DataFrame-ul gol pentru a completa toate combinațiile posibile
    df = pd.merge(empty_df, dfx, how='left', on=['Order Date', 'state_id'])

    # Gruparea după lună și stat, calcularea sumei profitului și resetarea indexului
    result_df = df.groupby([pd.to_datetime(df["Order Date"]).dt.to_period("M"), "state_id"])[
        "Profit"].sum().reset_index()

    fig = px.bar(result_df, x="state_id", y="Profit", color="Profit",
      animation_frame="Order Date", animation_group="state_id", range_y=[min(result_df["Profit"].tolist()), max(result_df["Profit"].tolist())])
    fig.show()

# Exemplu fictiv pentru funcția get_all_states

def harta_vanzari_pe_luna():
    # Datele tale
    dfx = get_data_with_state_id()

    # Adaugă codurile de stare lipsă pentru fiecare lună
    all_states = dfx["state_id"].drop_duplicates().tolist()
    all_dates = pd.date_range(start=dfx["Order Date"].min(), end=dfx["Order Date"].max(), freq='D')

    product = pd.MultiIndex.from_product([all_dates, all_states], names=['Order Date', 'state_id'])
    empty_df = pd.DataFrame(index=product).reset_index()

    # Uneste datele existente cu DataFrame-ul gol pentru a completa toate combinațiile posibile
    df = pd.merge(empty_df, dfx, how='left', on=['Order Date', 'state_id'])

    # Gruparea după lună și stat, calcularea sumei profitului și resetarea indexului
    result_df = df.groupby([pd.to_datetime(df["Order Date"]).dt.to_period("M"), "state_id"])[
        "Sales"].sum().reset_index()

    fig = px.choropleth(result_df,
                        locations='state_id',
                        color='Sales',
                        hover_name='state_id',
                        locationmode="USA-states",
                        title='Vanzari pe state in fiecare luna',
                        scope="usa",
                        animation_frame="Order Date",
                        color_continuous_scale='Viridis',  # Alegeți o hartă de culori (puteți utiliza și altele)
                        range_color=[min(result_df["Sales"].tolist()), max(result_df["Sales"].tolist())]  # Înlocuiți min_value și max_value cu limitele dorite
                        )

    fig.show()

