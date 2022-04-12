import dash 
from dash import html, callback
import base64
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

image_file_1 = 'other_pages/viz_image.jpeg'
image_file_2 = 'other_pages/viz_image_2.jpeg'
image_encoded_1 = base64.b64encode(open(image_file_1, 'rb').read())
image_encoded_2 = base64.b64encode(open(image_file_2, 'rb').read())

layout = html.Div(children=[

    dbc.CardHeader(dbc.Button('Load Visualization', color="primary", id="button-question-1", style={'color': 'White', 'fontSize': 20, 'textAlign': 'center'})),
    dbc.Collapse(html.Div([    
    html.Br(),
    html.Div('To load a saved plot click on the load viz button and choose from the list of saved visulizations from the popup dropdown menu', style={'fontSize':25, 'textAlign': 'left'}),
    # html.Br(),
    html.Div('See a description of doing this below', style={'fontSize':25, 'textAlign': 'left'}),
    html.Br(),
    html.Br(),
    html.Img(src='data:image/jpeg;base64,{}'.format(image_encoded_1.decode()), style={"width": "80rem"}), 
    html.Br(),
    html.Br(),
    ]), id="collapse-question-1", is_open=False),
    html.Hr(),
    
    dbc.CardHeader(dbc.Button('Saving Visualization', color="primary", id="button-question-2", style={'color': 'White', 'fontSize': 20, 'textAlign': 'center'})),
    dbc.Collapse(html.Div([
    html.Br(),
    html.Div('To save a plot click on the save viz button and type in a name to save your plot', style={'fontSize':25, 'textAlign': 'left'}),
    html.Div('See a description of doing this below', style={'fontSize':25, 'textAlign': 'left'}),
    html.Br(),
    html.Br(),    
    html.Img(src='data:image/jpeg;base64,{}'.format(image_encoded_2.decode()), style={"width": "80rem"})
    
    ]), id="collapse-question-2", is_open=False),
    html.Hr(),
    
    ])

@callback(
    [Output(f"collapse-question-{i}", "is_open") for i in range(1,3)],
    [Input(f"button-question-{i}", "n_clicks") for i in range(1,3)],
    [State(f"collapse-question-{i}", "is_open") for i in range(1,3)],
    
    )

def toggle_collapse(n1, n2, is_open1, is_open2):
    ctx = dash.callback_context
    
    if not ctx.triggered:
        return False, False
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
        
    if button_id == "button-question-1" and n1:
        return not is_open1, False
    elif button_id == "button-question-2" and n2:
        return False, not is_open2
    return False, False









