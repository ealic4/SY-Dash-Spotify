import dash
import plotly.express as px
import plotly.io as pio
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

col_list = ["genre", "loudness", "speechiness"]
df = pd.read_csv("genres_v2.csv", usecols=col_list)

genreloudness = px.bar(
    data_frame=df,
    x="genre",
    y="loudness",
    opacity=0.75,
    orientation="v",
    barmode='relative',
    labels={"loudness":"Loudness",
    "genre":"Genre"},
    title='Loudness-Genre',
    width=720,
    height=380,
    template='gridon')

glchrt = html.Div([dcc.Graph(
        id='example-graph',
        figure=genreloudness
    )])