import dash
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

from navbar import navbar
#from barchart import glchrt

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(children=[
#    #html.Div([navbar]),
   navbar,
 #  glchrt
#    #html.P('I am a component of the layout as well'),
    #dcc.Input(id='my=input', placeholder='Enter a value')
#])

])

if __name__ == '__main__':
    app.run_server(port=8080, debug=True)
