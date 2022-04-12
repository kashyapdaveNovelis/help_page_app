from dash import html
import base64

file_1 = 'other_pages/drill_image_1.jpeg'
file_2 = 'other_pages/drill_image_2.jpeg'

encoded_1 = base64.b64encode(open(file_1, 'rb').read())
encoded_2 = base64.b64encode(open(file_2, 'rb').read())

layout = html.Div(children= [
    
    html.H2('Using The Drill Down Functionality', style={'color': 'Blue', 'fontSize': 40, 'textAlign': 'center'}),
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
    
    ])

