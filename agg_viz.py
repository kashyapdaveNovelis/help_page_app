import dash
from dash import html, callback
import base64
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State


file_01 = 'other_pages/agg_image_01.jpeg'
encoded_01 = base64.b64encode(open(file_01, 'rb').read())
file_02 = 'other_pages/agg_image_02.jpeg'
encoded_02 = base64.b64encode(open(file_02, 'rb').read())
file_03 = 'other_pages/agg_image_03.jpeg'
encoded_03 = base64.b64encode(open(file_03, 'rb').read())
file_04 = 'other_pages/agg_image_04.jpeg'
encoded_04 = base64.b64encode(open(file_04, 'rb').read())


file_1 = 'other_pages/drill_image_1.jpeg'
file_2 = 'other_pages/drill_image_2.jpeg'

encoded_1 = base64.b64encode(open(file_1, 'rb').read())
encoded_2 = base64.b64encode(open(file_2, 'rb').read())



layout = html.Div(children= [
    
    dbc.CardHeader(dbc.Button('Aggregation Plot', color="primary", id="button-ques-1", style={'color': 'White', 'fontSize': 20, 'textAlign': 'center'})),
    dbc.Collapse(html.Div([
    
    html.Br(),
    html.H3('Description ', style={'fontSize':30, 'textAlign': 'left'}),
    html.Div('Aggregate toggle button: User can use it to enable aggregation of data for plots', style={'fontSize':25, 'textAlign': 'left'}),
    html.Div('Aggregation: User can choose how to aggregate data for plots from the available options', style={'fontSize':25, 'textAlign': 'left'}),
    html.Div('Aggregation key: User can choose one or more signals to aggregate the data used for the plots', style={'fontSize':25, 'textAlign': 'left'}),
    html.Br(),
    html.Br(),
    html.H3('Batch id melter vs average controls bathtemppv dg melter and average holder bathtemppv dg holder', style={'textAlign':'left tab', 'fontSize':30}),
    html.Br(),
    html.Img(src='data:image/jpeg;base64,{}'.format(encoded_01.decode()), style={"width": "80rem"}),   
    html.Br(),
    html.Br(),
    html.Br(),
    html.H3('KDE plot of average heat demand DG for each system Alloy DG', style={'textAlign':'left tab','fontSize':30}),
    html.Br(),
    html.Img(src='data:image/jpeg;base64,{}'.format(encoded_02.decode()), style={"width": "80rem"}),   
    html.Br(),
    html.Br(),  
    html.Br(),      
    html.H3('Box plot of average recipe water conventional total flow2 CG for each system alloy DG', style={'textAlign':'left tab', 'fontSize':30}),
    html.Br(),
    html.Img(src='data:image/jpeg;base64,{}'.format(encoded_03.decode()), style={"width": "80rem"}),   
    html.Br(),
    html.Br(), 
    html.Br(),
    html.H3('Box plot of average controls bathtempvc DG for each melter', style={'textAlign':'left tab', 'fontSize':30}),
    html.Br(),
    html.Img(src='data:image/jpeg;base64,{}'.format(encoded_04.decode()), style={"width": "80rem"}),   
    html.Br(),
    html.Br(), 
    ]), id="ques-1", is_open=False),
    html.Hr(), 
    
    dbc.CardHeader(dbc.Button('Drilldown', color="primary", id="button-ques-2", style={'color': 'White', 'fontSize': 20, 'textAlign': 'center'})),
    dbc.Collapse(html.Div([
    
    # html.H2('Using The Drill Down Functionality', style={'color': 'Blue', 'fontSize': 40, 'textAlign': 'center'}),
    html.Br(),
    html.Div("To use the drill down button first select a data point from a plot. The point's coil/batch id will be selected on the left bottom corner of the plot", style={'fontSize':25, 'textAlign': 'left'}),
    html.Br(),
    html.Img(src='data:image/jpeg;base64,{}'.format(encoded_1.decode()), style={"width": "80rem"}),
    html.Br(),
    html.Br(),
    html.Div("After selecting a point on the plot click the drill down button to see a detailed plot of the point's signals as below", style={'fontSize':25, 'textAlign': 'left'}),
    html.Br(),
    html.Br(),    
    html.Img(src='data:image/jpeg;base64,{}'.format(encoded_2.decode()), style={"width": "80rem"})
    ]), id="ques-2", is_open=False),
    html.Hr(), 
    
    ])

@callback(
    [Output(f"ques-{i}", "is_open") for i in range(1,3)],
    [Input(f"button-ques-{i}", "n_clicks") for i in range(1,3)],
    [State(f"ques-{i}", "is_open") for i in range(1,3)],
    
    )

def toggle_collapse(n1, n2, is_open1, is_open2):
    ctx = dash.callback_context
    
    if not ctx.triggered:
        return False, False
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
        
    if button_id == "button-ques-1" and n1:
        return not is_open1, False
    elif button_id == "button-ques-2" and n2:
        return False, not is_open2
    return False, False


    


