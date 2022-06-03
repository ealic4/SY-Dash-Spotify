import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

from navbar import navbar
from barchart import glchrt

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div(children=[
   navbar,
   dbc.Row([dbc.Col([dbc.Row(glchrt),dbc.Row(["Graf2"])]),dbc.Col([dbc.Row([

    dcc.Textarea(
        id='textarea-example1',
        value='Ovaj bar-chart pokazuje atribut loudness kroz razlicite muzicke zanrove. Atribut loudness je uglavnom negativan.',
        style={'width': 250, 'height': 150, 'border': 0, 'marginTop': 100, 'text-align':'justify'},
    ),
    html.Div(id='textarea-example-output1', style={'whiteSpace': 'pre-line'})


]),
       dbc.Row([
           html.Div([dcc.Textarea(
        id='textarea-example2',
        value='Textarea content initialized\nwith multiple lines of text',
        style={'width': 250, 'height': 150, 'margin-top': 150, 'border': 0 , 'text-align':'justify'},
    ),
    html.Div(id='textarea-example-output2', style={'whiteSpace': 'pre-line'})
])

])]), dbc.Col([html.Div([
        dcc.Textarea(
        id='textarea-example',
        value = 'The key improvement of SimpleText over TeachText was the addition of text styling. The underlying OS required by SimpleText implemented\The key improvement of SimpleText over TeachText was the addition of text styling. The underlying OS required by SimpleText implemented. SimpleText over TeachText was the addition of text styling. The underlying OS required by SimpleText implemented.',
        style={'width': 250, 'height': 400, 'border': 0, 'marginTop': 100, 'text-align':'justify'},
    ),
    html.Div(id='textarea-example-output', style={'whiteSpace': 'pre-line'})
])])])
])


if __name__ == '__main__':
    app.run_server(port=8080, debug=True)
