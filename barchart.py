import plotly.express as px
import pandas as pd
from dash import dcc, html

col_list = ["genre", "loudness"]
df = pd.read_csv("genres_v2.csv", usecols=col_list)

#listnumber = df['genre'].value_counts(ascending=False)
#print(listnumber)
#dff = df.groupby(["genre"]).loudness.sum().reset_index()

lista = df['genre']
listgenre = list(dict.fromkeys(lista))

df["loudness"] = df["loudness"]*(-1)
lista = df.groupby('genre')['loudness'].mean()

df = pd.DataFrame({
    "genre": listgenre,
    "loudness_mean": lista})

genreloudness = px.bar(
    data_frame=df,
    x="genre",
    y="loudness_mean",
    opacity=0.75,
    orientation="v",
    barmode='relative',
    labels={"loudness_mean":"Loudness",
    "genre":"Genre"},
    title='Loudness-Genre Distribution',
    width=720,
    height=380,
    template='gridon')


glchrt = html.Div([dcc.Graph(
        id='example-graph',
        figure=genreloudness
    )])
