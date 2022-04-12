from dash import html, callback
import base64
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State


image_file = 'other_pages/bin_trend_image.jpeg'
image_encoded = base64.b64encode(open(image_file, 'rb').read())

layout = html.Div(children= [
    
    dbc.CardHeader(dbc.Button('Binning and Trendlines', color="primary", id="button-question-1", style={'color': 'White', 'fontSize': 20, 'textAlign': 'center'})),
    dbc.Collapse(html.Div([
    html.Br(),
    html.H2('Description ', style={'fontSize':30, 'textAlign': 'left'}),
    html.Div('Bin: User can use this aggregate feature to choose the number of bins for plots', style={'fontSize':25, 'textAlign': 'left'}),
    html.Div('Trendline: User can use this aggregate feature to pick an option to use for the plotted line', style={'fontSize':25, 'textAlign': 'left'}),
    html.Br(),
    html.Br(),
    html.Img(src='data:image/jpeg;base64,{}'.format(image_encoded.decode()), style={"width": "80rem"}), 
    html.Br(),
    html.Br(),
    ]), id="coll-quest-1", is_open=False),
    html.Hr(),
    
    
    ])

@callback(
    Output("coll-quest-1", "is_open"),
    [Input("button-question-1", "n_clicks")],
    [State("coll-quest-1", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

