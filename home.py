import dash
import base64
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html, callback
from dash.dependencies import Input, Output, State


app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.MATERIA])

_filename_1 = 'machine_image_1.jpeg' 
_filename_2 = 'machine_image_2.jpeg'
_filename_3 = 'machine_image_3.jpeg'
_filename_4 = 'machine_image_4.jpeg'


encod_image_1 = base64.b64encode(open(_filename_1, 'rb').read())
encod_image_2 = base64.b64encode(open(_filename_2, 'rb').read())
encod_image_3 = base64.b64encode(open(_filename_3, 'rb').read())
encod_image_4 = base64.b64encode(open(_filename_4, 'rb').read())

_file_1 = 'gloss_image_1.jpeg'
_encoded_1 = base64.b64encode(open(_file_1, 'rb').read())
_file_2 = 'gloss_image_2.jpeg'
_encoded_2 = base64.b64encode(open(_file_2, 'rb').read())
_file_3 = 'gloss_image_3.jpeg'
_encoded_3 = base64.b64encode(open(_file_3, 'rb').read())

image_file_1 = 'viz_image.jpeg'
image_file_2 = 'viz_image_2.jpeg'
img_encoded_1 = base64.b64encode(open(image_file_1, 'rb').read())
img_encoded_2 = base64.b64encode(open(image_file_2, 'rb').read())

image_filename_1 = 'image_1.jpeg' 
image_filename_2 = 'image_2.jpeg'
image_filename_3 = 'image_3.jpeg'
image_filename_4 = 'image_4.jpeg'
image_filename_5 = 'image_5.jpeg'


encoded_image_1 = base64.b64encode(open(image_filename_1, 'rb').read())
encoded_image_2 = base64.b64encode(open(image_filename_2, 'rb').read())
encoded_image_3 = base64.b64encode(open(image_filename_3, 'rb').read())
encoded_image_4 = base64.b64encode(open(image_filename_4, 'rb').read())
encoded_image_5 = base64.b64encode(open(image_filename_5, 'rb').read())

file_01 = 'agg_image_01.jpeg'
encoded_01 = base64.b64encode(open(file_01, 'rb').read())
file_02 = 'agg_image_02.jpeg'
encoded_02 = base64.b64encode(open(file_02, 'rb').read())
file_03 = 'agg_image_03.jpeg'
encoded_03 = base64.b64encode(open(file_03, 'rb').read())
file_04 = 'agg_image_04.jpeg'
encoded_04 = base64.b64encode(open(file_04, 'rb').read())


file_1 = 'drill_image_1.jpeg'
file_2 = 'drill_image_2.jpeg'

encoded_1 = base64.b64encode(open(file_1, 'rb').read())
encoded_2 = base64.b64encode(open(file_2, 'rb').read())

image_file_1 = 'bin_trend_image.jpeg'
image_file_2 = 'raw_coil_image.jpeg'
image_encoded_1 = base64.b64encode(open(image_file_1, 'rb').read())
image_encoded_2 = base64.b64encode(open(image_file_2, 'rb').read())

im_file_1 = 'join_image_1.jpeg'
im_encoded_1 = base64.b64encode(open(im_file_1, 'rb').read())
im_file_2 = 'join_image_2.jpeg'
im_encoded_2 = base64.b64encode(open(im_file_2, 'rb').read())
im_file_3 = 'join_image_3.jpeg'
im_encoded_3 = base64.b64encode(open(im_file_3, 'rb').read())
im_file_4 = 'join_image_4.jpeg'
im_encoded_4 = base64.b64encode(open(im_file_4, 'rb').read())

#styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "23rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
    'fontSize':23
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "28rem",
    "margin-right": "5rem",
    "padding": "3rem 2rem",
}

sidebar = html.Div(
    [
        html.H3("Help Panel", className="display-6", style={'fontSize':30}),
        html.Hr(),
        html.P(
            "Choose from the help options available", className="lead", style={'fontSize':20, 'textAlign': 'left'}
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Tagging Functionality", href="/loading_viz", active="exact"),
                dbc.NavLink("Length Time Filters", href="/lenght_filter_viz", active="exact"),
                dbc.NavLink("Aggregate And Drilldown", href="/agg_drill_viz", active="exact"),
                dbc.NavLink("Coil Based Plot", href="/coil_viz", active="exact"),
                dbc.NavLink("Joins", href="/join_viz", active="exact"),
                dbc.NavLink("Aggregation", href="/agg_viz", active="exact"),
                
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


layout_1 = html.Div(children= [

    html.H1('WELCOME TO THE EAGLE VIZ HELP PAGE', 
            style={'color': 'Blue', 'fontSize': 40, 'textAlign': 'center'}),
    html.Br(),
    html.Div("You can find out information and tutorials \
             about the functionality for developing plots, retrieving and downloading data from \
             Novelis' Local and Global plants", style={'fontSize':25, 'textAlign': 'center'}),
    
    html.Br(),    
    html.Div('Below are the features of Eagle Viz interface', style={'textAlign':'left tab', 'fontSize':25}),
    html.Br(),
    html.Img(src='data:image/jpeg;base64,{}'.format(_encoded_1.decode()), style={"width": "80rem"}),   
    html.Br(),
    html.Br(),
    html.Br(),
    html.Img(src='data:image/jpeg;base64,{}'.format(_encoded_2.decode()), style={"width": "80rem"}),   
    html.Br(),
    html.Br(),
    html.Br(),
    html.Img(src='data:image/jpeg;base64,{}'.format(_encoded_3.decode()), style={"width": "80rem"}),   
    html.Br(),
    html.Br(),
    
    
    ])
            
             
layout_2 = html.Div(children=[

    dbc.CardHeader(dbc.Button('Load Visualization', color="primary", id="butt-question-1", \
        style={'color': 'White', 'fontSize': 22, 'textAlign': 'center'}), style={'text-align':'center'}),
    dbc.Collapse(html.Div([    
    html.Br(),
    html.Div('To load a saved plot click on the load viz button and choose from the list of saved visulizations from the popup dropdown menu', style={'fontSize':25, 'textAlign': 'left'}),
    html.Div('See a description of doing this below', style={'fontSize':25, 'textAlign': 'left'}),
    html.Br(),
    html.Br(),
    html.Img(src='data:image/jpeg;base64,{}'.format(img_encoded_1.decode()), style={"width": "80rem"}), 
    html.Br(),
    html.Br(),
    ]), id="collapse-question-1", is_open=False),
    html.Hr(),
    
    dbc.CardHeader(dbc.Button('Saving Visualization', color="primary", id="butt-question-2", \
        style={'color': 'White', 'fontSize': 22, 'textAlign': 'center'}), style={'text-align':'center'}),
    dbc.Collapse(html.Div([
    html.Br(),
    html.Div('To save a plot click on the save viz button and type in a name to save your plot', style={'fontSize':25, 'textAlign': 'left'}),
    html.Div('See a description of doing this below', style={'fontSize':25, 'textAlign': 'left'}),
    html.Br(),
    html.Br(),    
    html.Img(src='data:image/jpeg;base64,{}'.format(img_encoded_2.decode()), style={"width": "80rem"})
    
    ]), id="collapse-question-2", is_open=False),
    html.Hr(),
    
    ])

layout_3 = html.Div(children=[
    
    dbc.CardHeader(dbc.Button('Length Filter', color="primary", id="b-question-1", \
        style={'color': 'White', 'fontSize': 22, 'textAlign': 'center'}), style={'text-align':'center'}),
    dbc.Collapse(html.Div([
    html.Br(),
    html.H2('Description ', style={'fontSize':30, 'textAlign': 'left'}),
    html.Div('Length Filters: User can either specify an absolute value or percentage - E.g. 100 to 200 or 25% to 75%', style={'fontSize':25, 'textAlign': 'left'}),
    html.Br(),  
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
    
    dbc.CardHeader(dbc.Button('Time Filter', color="primary", id="b-question-2", \
        style={'color': 'White', 'fontSize': 22, 'textAlign': 'center'}), style={'text-align':'center'}),
    dbc.Collapse(html.Div([
    html.Br(),
    html.H2('Description ', style={'fontSize':30, 'textAlign': 'left'}),
    html.Div('Time Filters: User can specify time in HH:MM:SS (24 Hour) format - E.g. 06:00:00', style={'fontSize':25, 'textAlign': 'left'}),
    html.Br(),
    html.Br(),
    html.H3('Time vs eg F1 totalbending', style={'textAlign':'left tab', 'fontSize':30}),
    html.Br(),
    html.Img(src='data:image/jpeg;base64,{}'.format(encoded_image_5.decode()), style={"width": "80rem"})    
    ]), id="question-2", is_open=False),
    html.Hr(),
            
    ])


layout_4 = html.Div(children= [
    
    dbc.CardHeader(dbc.Button('Aggregation Plot', color="primary", id="button-ques-1", \
        style={'color': 'White', 'fontSize': 22, 'textAlign': 'center'}), style={'text-align':'center'}),
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
    
    dbc.CardHeader(dbc.Button('Drilldown', color="primary", id="button-ques-2", \
        style={'color': 'White', 'fontSize': 22, 'textAlign': 'center'}), style={'text-align':'center'}),
    dbc.Collapse(html.Div([
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

layout_5 = html.Div(children= [
    
    dbc.CardHeader(dbc.Button('Aggregate Binning And Trendlines', color="primary", id="button-quest-1", \
        style={'color': 'White', 'fontSize': 22, 'textAlign': 'center'}), style={'text-align':'center'}),
    dbc.Collapse(html.Div([
    html.Br(),
    html.H2('Description ', style={'fontSize':30, 'textAlign': 'left'}),
    html.Div('Aggregate bucket size: User can use this aggregate feature to choose the bucket size for plots with aggregated data tables', style={'fontSize':25, 'textAlign': 'left'}),
    html.Div('Trendline: User can use this feature to choose the plotted line for the aggregated data plot', style={'fontSize':25, 'textAlign': 'left'}),
    html.Br(),
    html.Br(),
    html.Img(src='data:image/jpeg;base64,{}'.format(image_encoded_1.decode()), style={"width": "80rem"}), 
    html.Br(),
    html.Br(),
    ]), id="coll-quest-1", is_open=False),
    html.Hr(),
    
    dbc.CardHeader(dbc.Button('Raw Coil Visualization', color="primary", id="button-quest-2", \
        style={'color': 'White', 'fontSize': 22, 'textAlign': 'center'}), style={'text-align':'center'}),
    dbc.Collapse(html.Div([
    html.Br(),
    html.Div('To visualize a raw coil visualization plot choose one or more coil and batch ids from the dropdown after selecting a plant and machine center', style={'fontSize':25, 'textAlign': 'left'}),
    html.Br(),
    html.Br(),
    html.H3('Time vs eg F1 totalbending',style={'textAlign':'left tab', 'fontSize':30}),
    html.Br(),
    html.Img(src='data:image/jpeg;base64,{}'.format(image_encoded_2.decode()), style={"width": "80rem"}), 
    html.Br(),
    html.Br(),
    ]), id="coll-quest-2", is_open=False),
    html.Hr(),
    
    
    ])

layout_6 = html.Div(children= [
    
        
    dbc.CardHeader(dbc.Button('Join Visualization', color="primary", id="button-question-1", \
        style={'color': 'White', 'fontSize': 22, 'textAlign': 'center'}), style={'text-align':'center'}),
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


layout_7 = html.Div(children=[

    dbc.CardHeader(dbc.Button('Single Machine Center', color="primary", id="bu-question-1", \
        style={'color': 'White', 'fontSize': 22, 'textAlign': 'center'}), style={'text-align':'center'}),
    dbc.Collapse(html.Div([    
    html.Br(),
    html.Div('To load plots by choosing a single machine center from the machine center dropdown use the defaults or choose one or more signals for the aggregate settings', style={'fontSize':25, 'textAlign': 'left'}),
    html.Div('See a description of doing this below for default and custom aggregate keys', style={'fontSize':25, 'textAlign': 'left'}),
    html.Br(),
    html.Br(),
    html.H3('Box plot of average dg entemp temperature measure for each cg gen alloy', style={'textAlign':'left tab', 'fontSize':30}),
    html.Br(),
    html.Img(src='data:image/jpeg;base64,{}'.format(encod_image_1.decode()), style={"width": "80rem"}), 
    html.Br(),
    html.Br(),
    html.H3('Box plot of average controls bathtempcv dg for each melter', style={'textAlign':'left tab', 'fontSize':30}),
    html.Br(),
    html.Img(src='data:image/jpeg;base64,{}'.format(encod_image_2.decode()), style={"width": "80rem"}), 
    html.Br(),
    html.Br(),
    ]), id="co-question-1", is_open=False),
    html.Hr(),
    
    dbc.CardHeader(dbc.Button('Multiple Machine Centers', color="primary", id="bu-question-2", \
        style={'color': 'White', 'fontSize': 22, 'textAlign': 'center'}), style={'text-align':'center'}),
    dbc.Collapse(html.Div([
    html.Br(),
    html.Div('To load plots by choosing multiple machine centers from the machine center dropdown use the defaults or choose one or more signals for the aggregate settings', style={'fontSize':25, 'textAlign': 'left'}),
    html.Div('See a description of doing this below for default aggregate keys and for using left and right join keys', style={'fontSize':25, 'textAlign': 'left'}),
    html.Br(),
    html.Br(), 
    html.H3('Eg Lenghtindex HFM Bin vs Average DG Exshape Actualflatness CM3 & Average DG exprofile Absolute raw profile HFM', style={'textAlign':'left tab', 'fontSize':30}),
    html.Br(),
    html.Img(src='data:image/jpeg;base64,{}'.format(encod_image_3.decode()), style={"width": "80rem"}),
    html.Br(),
    html.Br(),
    html.H3('Eg Lenghtindex CM3 vs eg st1 totalbending CM3 and Eg F1 totalbending HFM', style={'textAlign':'left tab', 'fontSize':30}),
    html.Br(),    
    html.Img(src='data:image/jpeg;base64,{}'.format(encod_image_4.decode()), style={"width": "80rem"}),
    html.Br(),
    html.Br()    
    ]), id="co-question-2", is_open=False),
    html.Hr(),
    
    ])


content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content,
    
])


@callback(
    Output("page-content", "children"),
    [Input("url", "pathname")])
    
def render_page_content(pathname):
    if pathname == "/":
        return layout_1
    elif pathname == '/loading_viz':
        return layout_2
    elif pathname == '/lenght_filter_viz':
        return layout_3 
    if pathname == '/agg_drill_viz':
        return layout_4
    if pathname == '/coil_viz':
        return layout_5
    if pathname == '/join_viz':
        return layout_6
    if pathname == '/agg_viz':
        return layout_7
    else:
        return "404 Page Error! Please choose a link"


@callback(
    [Output(f"collapse-question-{i}", "is_open") for i in range(1,3)],
    [Input(f"butt-question-{i}", "n_clicks") for i in range(1,3)],
    [State(f"collapse-question-{i}", "is_open") for i in range(1,3)],
    
    )

def toggle_collapse_1(n1, n2, is_open1, is_open2):
    ctx = dash.callback_context
    
    if not ctx.triggered:
        return False, False
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
        
    if button_id == "butt-question-1" and n1:
        return not is_open1, False
    elif button_id == "butt-question-2" and n2:
        return False, not is_open2
    return False, False


@callback(
    [Output(f"question-{i}", "is_open") for i in range(1,3)],
    [Input(f"b-question-{i}", "n_clicks") for i in range(1,3)],
    [State(f"question-{i}", "is_open") for i in range(1,3)],
    
    )

def toggle_collapse_2(n1, n2, is_open1, is_open2):
    ctx = dash.callback_context
    
    if not ctx.triggered:
        return False, False
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
        
    if button_id == "b-question-1" and n1:
        return not is_open1, False
    elif button_id == "b-question-2" and n2:
        return False, not is_open2
    return False, False

@callback(
    [Output(f"ques-{i}", "is_open") for i in range(1,3)],
    [Input(f"button-ques-{i}", "n_clicks") for i in range(1,3)],
    [State(f"ques-{i}", "is_open") for i in range(1,3)],
    
    )

def toggle_collapse_3(n1, n2, is_open1, is_open2):
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


@callback(
    [Output(f"coll-quest-{i}", "is_open") for i in range(1,3)],
    [Input(f"button-quest-{i}", "n_clicks") for i in range(1,3)],
    [State(f"coll-quest-{i}", "is_open") for i in range(1,3)],
    
    )

def toggle_collapse_4(n1, n2, is_open1, is_open2):
    ctx = dash.callback_context
    
    if not ctx.triggered:
        return False, False
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
        
    if button_id == "button-quest-1" and n1:
        return not is_open1, False
    elif button_id == "button-quest-2" and n2:
        return False, not is_open2
    return False, False


@callback(
    Output("colla-ques-1", "is_open"),
    [Input("button-question-1", "n_clicks")],
    [State("colla-ques-1", "is_open")],
)
def toggle_collapse_5(n, is_open):
    if n:
        return not is_open
    return is_open

@callback(
    [Output(f"co-question-{i}", "is_open") for i in range(1,3)],
    [Input(f"bu-question-{i}", "n_clicks") for i in range(1,3)],
    [State(f"co-question-{i}", "is_open") for i in range(1,3)],
    
    )

def toggle_collapse_6(n1, n2, is_open1, is_open2):
    ctx = dash.callback_context
    
    if not ctx.triggered:
        return False, False
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
        
    if button_id == "bu-question-1" and n1:
        return not is_open1, False
    elif button_id == "bu-question-2" and n2:
        return False, not is_open2
    return False, False


if __name__=='__main__':
    app.run_server(port=3000, debug=True, dev_tools_hot_reload=True)