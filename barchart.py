import plotly.express as px
import pandas as pd
from dash import dcc, html


col_list = ["genre", "loudness"]
df = pd.read_csv("genres_v2.csv", usecols=col_list)
df["loudness"] = df["loudness"].abs()

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