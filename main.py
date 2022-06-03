import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

from navbar import navbar
#from barchart import glchrt

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div(children=[
   navbar,
dbc.Row([dbc.Col([dbc.Row(["Graf1"]),dbc.Row(["Graf2"])]),dbc.Col([dbc.Row([

    dcc.Textarea(
        id='textarea-example1',
        value='Textarea content initialized\nwith multiple lines of text',
        style={'width': '100%', 'height': 100},
    ),
    html.Div(id='textarea-example-output1', style={'whiteSpace': 'pre-line'})


]),dbc.Row([

html.Div([
    dcc.Textarea(
        id='textarea-example2',
        value='Textarea content initialized\nwith multiple lines of text',
        style={'width': '100%', 'height': 100, 'margina-top':50},
    ),
    html.Div(id='textarea-example-output2', style={'whiteSpace': 'pre-line'})
])









])]),dbc.Col([html.Div([
    dcc.Textarea(
        id='textarea-example',
        value='Textarea content initialized\nwith multiple lines of text',
        style={'width': '100%', 'height': 300},
    ),
    html.Div(id='textarea-example-output', style={'whiteSpace': 'pre-line'})
])])])
])


if __name__ == '__main__':
    app.run_server(port=8080, debug=True)
