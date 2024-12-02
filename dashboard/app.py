# ------------------------------------------------
# List imports
#-------------------------------------------------
import plotly.express as px
import random
import seaborn as sns
import pandas as pd
from shiny import reactive
from shiny.express import render, input, ui
from shinywidgets import render_plotly
from datetime import datetime
from collections import deque
from scipy import stats
from faicons import icon_svg
# ------------------------------------------------
# Get the Data
#-------------------------------------------------
flights_df = pd.read_csv('flights.csv')
# -------------------------------------------------
# Reactive calculations and effects
# -------------------------------------------------
@reactive.calc
def filtered_year():
    selected_year=input.selected_year_list()
    if selected_year:
        filtered_df=flights_df[flights_df['flights'].isin(selected_year)]
    else:
        filtered_df=flights_df
    return filtered_df

@reactive_calc
def filtered_month():
    selected_month=input.selected_month_list()
    if selected_month:
        filtered_df=flights_df[flights_df['flights'].isin(selected_month)]
    else:
        filtered_df=flights_df
    return filtered_df
# ------------------------------------------------
# Define the Shiny UI Page layout - Page Options
# ------------------------------------------------
ui.page_opts(title="Pinkston's Custom PyShiny Plots with Flights", fillable=True)
# ------------------------------------------------
# Define the Shiny UI Page layout - Sidebar
# ------------------------------------------------
with ui.sidebar(position="right", open="open", bg="#d5d8dc"):
    ui.h2("Sidebar")

    ui.input_selectize(
        "selected_year_list",
        "Select a Year",
        ["1949", "1950", "1951", "1952", "1953", "1954", "1955", "1956", "1957", "1958", "1959", "1960"],
        multiple=True)
    
    ui.input_checkbox_group(
        "selected_month_list",
        "Filter by Month",
        ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        selected=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        inline=True)
    
    ui.hr()
    ui.a(
        "My Github Repository",
        href="https://github.com/james-0177/cintel-06-custom/tree/main",
        target='_blank')
    
# Main Content
with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header("Data Grid of Flights")
        @render.data_frame
        def grid():
             return render.DataGrid(data=filtered_year() + filtered_month())
        
with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header("Plotly Scatterplot: Flights")
        @render_plotly
        def plotly_scatterplot():
            return px.scatter(data_frame=filtered_year() + filtered_month(), x="month", y="year", color="passengers", hover_name="passengers")
#---------------------------------------------------------------------
# In Shiny Express, everything not in the sidebar is in the main panel
#---------------------------------------------------------------------
