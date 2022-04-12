from dash import html, callback
import base64
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State


im_file_1 = 'other_pages/join_image_1.jpeg'
im_encoded_1 = base64.b64encode(open(im_file_1, 'rb').read())
im_file_2 = 'other_pages/join_image_2.jpeg'
im_encoded_2 = base64.b64encode(open(im_file_2, 'rb').read())
im_file_3 = 'other_pages/join_image_3.jpeg'
im_encoded_3 = base64.b64encode(open(im_file_3, 'rb').read())
im_file_4 = 'other_pages/join_image_4.jpeg'
im_encoded_4 = base64.b64encode(open(im_file_4, 'rb').read())

layout = html.Div(children= [
    
        
    dbc.CardHeader(dbc.Button('Join Visualization', color="primary", id="button-question-1", style={'color': 'White', 'fontSize': 20, 'textAlign': 'center'})),
    dbc.Collapse(html.Div([
    
    html.Br(),
    html.H3('Description ', style={'fontSize':30, 'textAlign': 'left'}),
    html.Div('Join left key: User can choose a signal to perform a left join for the plotted data', style={'fontSize':25, 'textAlign': 'left'}),
    html.Div('Join right key: User can choose a signal to perform a right join for the plotted data', style={'fontSize':25, 'textAlign': 'left'}),
    html.Div('How: User can choose how they want the data for the plots should be joined', style={'fontSize':25, 'textAlign': 'left'}),
    html.Br(),
    html.Br(),
    html.H3('Eg Lenghtindex HFN Bin vs Average DG Exprofile Absolute raw profile HFM & Average DG exshape Actual flatness CM88', style={'textAlign':'left tab', 'fontSize':30}),
    html.Br(),
    html.Img(src='data:image/jpeg;base64,{}'.format(im_encoded_1.decode()), style={"width": "80rem"}),   
    html.Br(),
    html.Br(),
    html.Br(),
    html.H3('Eg Lenghtindex HFM Bin vs Average DG Exshape Actualflatness CM3 & Average DG exprofile Absolute raw profile HFM', style={'textAlign':'left tab', 'fontSize':30}),
    html.Br(),
    html.Img(src='data:image/jpeg;base64,{}'.format(im_encoded_2.decode()), style={"width": "80rem"}),   
    html.Br(),
    html.Br(),  
    html.Br(),      
    html.H3('Eg Lenghtindex CMM88 vs Average DG Exprofile Absolute raw profile HFM & Average DG exshape Actual flatness deviation CM88', style={'textAlign':'left tab', 'fontSize':30}),
    html.Br(),
    html.Img(src='data:image/jpeg;base64,{}'.format(im_encoded_3.decode()), style={"width": "80rem"}),   
    html.Br(),
    html.Br(), 
    html.Br(),
    html.H3('Eg Lenghtindex CMM88 Bin vs Average DG Exprofile Absolute raw profile HFM & Average DG exshape Actual flatness CM88', style={'textAlign':'left tab', 'fontSize':30}),
    html.Br(),
    html.Img(src='data:image/jpeg;base64,{}'.format(im_encoded_4.decode()), style={"width": "80rem"}),   
    html.Br(),
    html.Br(), 
    ]), id="colla-ques-1", is_open=False),
    html.Hr(),
    
    ])

@callback(
    Output("colla-ques-1", "is_open"),
    [Input("button-question-1", "n_clicks")],
    [State("colla-ques-1", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


