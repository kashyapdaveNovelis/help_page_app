from dash import html, callback
import base64
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

image_filename_1 = 'other_pages\image_1.jpeg' 
image_filename_2 = 'other_pages\image_2.jpeg'
image_filename_3 = 'other_pages\image_3.jpeg'
image_filename_4 = 'other_pages\image_4.jpeg'


encoded_image_1 = base64.b64encode(open(image_filename_1, 'rb').read())
encoded_image_2 = base64.b64encode(open(image_filename_2, 'rb').read())
encoded_image_3 = base64.b64encode(open(image_filename_3, 'rb').read())
encoded_image_4 = base64.b64encode(open(image_filename_4, 'rb').read())


layout = html.Div(children=[
    
    dbc.CardHeader(dbc.Button('Length Filter', color="primary", id="button-question-1", style={'color': 'White', 'fontSize': 20, 'textAlign': 'center'})),
    dbc.Collapse(html.Div([
    html.Br(),
    html.H2('Description ', style={'fontSize':30, 'textAlign': 'left'}),
    html.Div('Length Filters - User can either specify an absolute value or percentage - E.g. 100 to 200 or 25% to 75%', style={'fontSize':25, 'textAlign': 'left'}),
    html.Div('Time Filters - User can specify time in HH:MM:SS (24 Hour) format - E.g. 06:00:00', style={'fontSize':25, 'textAlign': 'left'}),
    html.Br(),   
    html.H3('Eg Lenghtindex Bin vs Average EG F3 Forwardsip and Average Eg F4 Forward Tension', style={'textAlign':'left tab', 'fontSize':30}),
    html.Br(),
    html.Img(src='data:image/jpeg;base64,{}'.format(encoded_image_1.decode()), style={"width": "80rem"}),
    html.Br(),
    html.Br(),
    html.H3('Average Eg F1 Total RollForce vs Average Eg F1 Exit Thickness', style={'textAlign':'left tab', 'fontSize':30}),
    html.Br(),
    html.Img(src='data:image/jpeg;base64,{}'.format(encoded_image_2.decode()), style={"width": "80rem"}),
    html.Br(),
    html.Br(),
    html.H3('Eg lenghtindex HFM Bin vs Average DG Exshape Actualflatness CM3 and Average Dc exprofile Absolute raw profile HFN', style={'textAlign':'left tab', 'fontSize':30}),
    html.Br(),
    html.Img(src='data:image/jpeg;base64,{}'.format(encoded_image_3.decode()), style={"width": "80rem"}),
    html.Br(),
    html.Br(),
    html.H3('Box plot of Eg exit Temperature Relative error for each CG gen Alloy', style={'textAlign':'left tab', 'fontSize':30}),
    html.Br(),
    html.Img(src='data:image/jpeg;base64,{}'.format(encoded_image_4.decode()), style={"width": "80rem"}),
    html.Br(),
    html.Br(),
    ]), id="question-1", is_open=False),
    html.Hr(),    
            
    ])


@callback(
    Output("question-1", "is_open"),
    [Input("button-question-1", "n_clicks")],
    [State("question-1", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open



