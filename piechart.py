import plotly.express as px
import pandas as pd
from dash import dcc, html
col_list = ["genre"]
df = pd.read_csv("genres_v2.csv", usecols=col_list)


lista = df['genre']

listgenre = list(dict.fromkeys(lista))
listnumber = df['genre'].value_counts(ascending=False)


df = pd.DataFrame({
    "genre": listgenre,
    "values": listnumber})

fig= px.pie(df, values='values', names='genre')

gl2chrt = html.Div([dcc.Graph(
        id='example-graph2',
        figure=fig
    )])








