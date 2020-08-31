# importing relevant packages
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

# importing linked files
from app import app, server
from tabs import tab1, tab2, tab3, tab4

style = {'maxWidth': '960px', 'margin': 'auto'}
# implementing tab structure
app.layout = html.Div([
    dcc.Markdown('# Track Popularity Predictor'),
    dcc.Tabs(id='tabs', value='tab1', children=[
        dcc.Tab(label='Intro', value='tab1', className = 'os-tab'),
        dcc.Tab(label='Development', value='tab2', className='os-tab'),
        dcc.Tab(label='Your track', value='tab3', className = 'os-tab'),
        dcc.Tab(label='Results', value='tab4', className = 'os-tab'),
    ]),
    html.Div(id='tabs-content'),
], style=style)

# go to tab on click
@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab1': return tab1.layout
    elif tab == 'tab2': return tab2.layout
    elif tab == 'tab3': return tab3.layout
    elif tab == 'tab4': return tab4.layout

# starting app
if __name__ == '__main__':
    app.run_server(debug=True)
