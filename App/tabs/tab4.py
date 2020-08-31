# importing relevant packages
from dash.dependencies import Input, Output
import dash_core_components as dcc
import pickle
import dash_html_components as html
import dash_bootstrap_components as dbc

# importing linked files
from app import app


# page set up
style = {'padding': '1.5em'}

layout = html.Div([

    html.Div([
        dcc.Markdown('### Predicted Popularity'),
        dcc.Textarea(
            id='popularity_prediction',
            style={'width': '100%', 'height': 100},
        ),
    ], style=style),

    html.Div([
        dcc.Markdown('### Similar Tracks'),
        html.Div(id='similar')],
        style=style),
    # artificial input so the page reloads the data everytime the tab is opened
    html.Div(id='input_dummy')
])


#loading output from tab3
@app.callback(
    [Output('popularity_prediction', 'value'),
     Output('similar', 'children')],
    [Input('input_dummy', 'value')])
def update_output(value):
    pred_pop = pickle.load(open('temp/pred_pop.pkl', 'rb'))
    similar=pickle.load(open('temp/similar.pkl', 'rb'))

    similar['cover'] = [html.Img(src=x,
                                 style={'height': '20%'}
                                 )
                        for x in similar['cover']
                        ]

    similar['preview'] = [html.A("Link to preview", href=x, target="_blank")
                          for x in similar['preview']
                          ]

    return pred_pop, dbc.Table.from_dataframe(similar, striped=True, bordered=True, hover=True, responsive="sm", size= 'sm')


