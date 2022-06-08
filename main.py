import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

from navbar import navbar
from barchart import glchrt
from piechart import gl2chrt
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div(children=[
   navbar,
   dbc.Row([dbc.Col([dbc.Row(glchrt),dbc.Row([gl2chrt])]),dbc.Col([dbc.Row([

    dcc.Textarea(
        id='textarea-example1',
        value='This chart shows the distribution of loudness attribute through different music genres. Since the loudness attribute is mostly negative, here is used the positive mean value.',
        style={'width': 250, 'height': 200, 'border': 0, 'marginTop': 100, 'text-align':'justify'},
    ),
    html.Div(id='textarea-example-output1', style={'whiteSpace': 'pre-line'})
]),
       dbc.Row([
           html.Div([dcc.Textarea(
        id='textarea-example2',
        value='This chart is showing the numbers of songs by genre. Did you know that Dark Trap is this popular?',
        style={'width': 250, 'height': 150, 'margin-top': 150, 'border': 0 , 'text-align':'justify'},
    ),
    html.Div(id='textarea-example-output2', style={'whiteSpace': 'pre-line'})
])

])]), dbc.Col([html.Div([
        dcc.Textarea(
        id='textarea-example',
        value = 'If you are a data lover, welcome to our page. Sign in or Register to show more tools and open more possibilities. The key improvement of SimpleText over TeachText was the addition of text styling. The underlying OS required by SimpleText implemented. SimpleText over TeachText was the addition of text styling. The underlying OS required by SimpleText implemented.',
        style={'width': 250, 'height': 400, 'border': 0, 'marginTop': 100, 'text-align':'justify'},
    ),
    html.Div(id='textarea-example-output', style={'whiteSpace': 'pre-line'})
])])])
])

if __name__ == '__main__':
    app.run_server(port=8080, debug=True)
