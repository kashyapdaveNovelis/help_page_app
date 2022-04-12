from dash import html
import base64

im_file_1 = 'other_pages/gloss_image_1.jpeg'
im_encoded_1 = base64.b64encode(open(im_file_1, 'rb').read())
im_file_2 = 'other_pages/gloss_image_2.jpeg'
im_encoded_2 = base64.b64encode(open(im_file_2, 'rb').read())
im_file_3 = 'other_pages/gloss_image_3.jpeg'
im_encoded_3 = base64.b64encode(open(im_file_3, 'rb').read())

layout = html.Div(children= [
    
    html.H1('WELCOME TO THE EAGLE VIZ HELP PAGE', 
            style={'color': 'Blue', 'fontSize': 40, 'textAlign': 'center'}),
    html.Br(),
    html.Div("You can find out information and tutorials \
             about the functionality for developing plots, retrieving and downloading data from \
             Novelis' Local and Global plants", style={'fontSize':25, 'textAlign': 'center'}),
    
    html.Br(),    
    html.Div('Below are the features of Eagle Viz interface', style={'textAlign':'left tab', 'fontSize':25}),
    html.Br(),
    html.Img(src='data:image/jpeg;base64,{}'.format(im_encoded_1.decode()), style={"width": "80rem"}),   
    html.Br(),
    html.Br(),
    html.Br(),
    html.Img(src='data:image/jpeg;base64,{}'.format(im_encoded_2.decode()), style={"width": "80rem"}),   
    html.Br(),
    html.Br(),
    html.Br(),
    html.Img(src='data:image/jpeg;base64,{}'.format(im_encoded_3.decode()), style={"width": "80rem"}),   
    html.Br(),
    html.Br(),
    
    
    ])

