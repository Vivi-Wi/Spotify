# importing relevant packages
import dash

# loading personal css stylesheet
external_stylesheets = ['https://codepen.io/vi-wi/pen/Rwapagd.css'] #originally: https://codepen.io/chriddyp/pen/bWLwgP.css']

# app set up
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True
server = app.server
