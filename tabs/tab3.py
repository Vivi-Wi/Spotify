# importing relevant packages
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pickle
import pandas as pd
from datetime import datetime as dt
import os,inspect

# importing linked files
from app import app

# cleaned cluster database from csv
cluster_database = pd.read_csv('data/cluster_database.csv')
cluster_database.drop('Unnamed: 0', axis=1, inplace=True)
cluster_database.reset_index(drop=True, inplace=True)

# options for genres
main_genres=['unspecified', 'electronic', 'hiphop', 'classical', 'rap', 'punk', 'house',
             'country', 'jazz', 'pop', 'disco', 'funk', 'rock', 'metal', 'audio book',
             'soul', 'r&b', 'sleep', 'latin', 'regional mexican', 'other']

cluster_columns=[ 'track', 'artists', 'cover', 'preview']

# page set up
style = {'padding': '1.5em'}

layout = html.Div([
    html.Div([
        dcc.Markdown("### Your Track"),
        dcc.Markdown("""Use the controls below to specify your track and predict its popularity.""")
    ],
        style=style),

# form
    html.Div([
        dcc.Markdown("###### Instrumental"),
        dcc.Slider(
            id='instrumentalness',
            min=0,
            max=1,
            step=0.01,
            value=0,
            marks={0: 'not intstrumental',
                   1: 'very instrumental'}
        ),
        dcc.Markdown("###### Speech"),
        dcc.Slider(
            id="speechiness",
            min=0,
            max=1,
            step=0.01,
            value=0,
            marks={0: "no spoken words",
                   1: "speech only"}
        ),
        dcc.Markdown("###### Acoustic"),
        dcc.Slider(
            id="acousticness",
            min=0,
            max=1,
            step=0.01,
            value=0,
            marks={0: "isn't acoustic",
                   1: "is acoustic"}
        ),
        dcc.Markdown("###### Live"),
        dcc.Slider(
            id="liveness",
            min=0,
            max=1,
            step=0.01,
            value=0,
            marks={0: "definitely studio!",
                   1: "concert"}
        ),
        dcc.Markdown("###### Energy"),
        dcc.Slider(
            id="energy",
            min=0,
            max=1,
            step=0.01,
            value=0,
            marks={0: "ZzZzZ",
                   1: "yay, party!"}
        ),
        dcc.Markdown("###### Danceability"),
        dcc.Slider(
            id="danceability",
            min=0,
            max=1,
            step=0.01,
            value=0,
            marks={0: "dinner party at most",
                   1: "let's boogy!"}
        ),
        dcc.Markdown("###### Loudness"),
        dcc.Slider(
            id="loudness",
            min=(-20),
            max=(-4),
            step=0.01,
            value=(-20),
            marks={(-20): "extremely loud",
                   (-4): "sound of silence"}
        ),
        dcc.Markdown("###### Duration"),
        dcc.Slider(
            id="duration_ms",
            min=92093,
            max=406109,
            step=0.01,
            value=92093,
            marks={92093: "short and sweet",
                   406109: "never ending"}
        ),
        dcc.Markdown("###### Tempo"),
        dcc.Slider(
            id="tempo",
            min=0,
            max=250,
            step=0.01,
            value=0,
            marks={0: "slowdance material",
                   250: "2 fast 2 furious"}
        ),
    ], style=style),

    html.Div([
        dcc.Markdown('###### Explicit'),
        dcc.RadioItems(
            id='explicit',
            options=[
                {'label': 'F**k yeah', 'value': '1'},
                {'label': 'Child proof', 'value': '0'},
            ],
            value='0'
        ),
    ], style=style),

    html.Div([
        dcc.Markdown("###### (Main) Genre"),
        dcc.Dropdown(
            id='main_genre',
            options=[{'label': genre, 'value': genre} for genre in main_genres],
            value='unspecified',
            style={'color':'black'},
        ),
    ], style=style),

    html.Div([
        dcc.Markdown('###### Release date'),
        dcc.DatePickerSingle(
            id='release_date',
            min_date_allowed=dt(2019, 1, 1),
            initial_visible_month=dt.today(),
            date=dt.today(),
        ),
    ], style=style),

    html.Div([
        dcc.Markdown('###### Total number of tracks in album'),
        dcc.Slider(
            id='total_album_tracks',
            min=1,
            max=20,
            step=1,
            value=1,
            marks={n: str(n) for n in range(1, 21, 1)}
        ),
    ], style=style),

    html.Div([
        dcc.Markdown('###### Track number in album'),
        dcc.Slider(
            id='album_track_no',
            min=1,
            max=20,
            step=1,
            value=1,
            marks={n: str(n) for n in range(1, 21, 1)}
        ),
    ], style=style),

    html.Div(id='test'),

    html.Div([
        html.Div(dbc.Button("submit for prediction", id="open"),
                 style={'textAlign': 'center'}),
        # popup telling you where to find the results
        dbc.Modal([
            dbc.ModalHeader("Submission successful!"),
            dbc.ModalBody("Please go to the 'Results'-tab to view your track's predicted popularity"
                          "and to listen to some similar tracks."),
            dbc.ModalFooter(dbc.Button("Close", id="close", className="ml-auto")),
        ],
            id="modal",
        ),
    ]),
])

# callback for the submit button
@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"),
     Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

# prediction callback
@app.callback(
    Output('test', 'value'),
    [Input('acousticness', 'value'),
     Input('album_track_no', 'value'),
     Input('danceability', 'value'),
     Input('duration_ms', 'value'),
     Input('energy', 'value'),
     Input('explicit', 'value'),
     Input('instrumentalness', 'value'),
     Input('liveness', 'value'),
     Input('loudness', 'value'),
     Input('speechiness', 'value'),
     Input('tempo', 'value'),
     Input('total_album_tracks', 'value'),
     Input('release_date', 'date'),
     Input('main_genre', 'value'),
     ])
def predict(acousticness, album_track_no, danceability, duration_ms, energy, explicit,
            instrumentalness, liveness, loudness, speechiness, tempo, total_album_tracks,
            release_date, main_genre):

    # features that were not included in the form
    time_signature=4                                    # median value
    place_in_album= album_track_no/total_album_tracks   # same calculation as in the model
    month= int(release_date.split("-")[1])              # same procedure as in the model
    if main_genre == main_genres[0]:
        no_genres = 0                                   # 0 if unspecified
    else:
        no_genres = 1                                   # median value for all main genres unless unspecified

    # putting the inputted data in the format needed by the model. Feature that are not used in the model
    # get placeholders
    df = pd.DataFrame(
        columns=['acousticness', 'album', 'album_track_no', 'artists', 'artists_id', 'available_markets',
                 'cover_url', 'danceability', 'duration_ms', 'energy', 'explicit', 'instrumentalness',
                 'liveness', 'loudness', 'name', 'preview_url', 'release_date', 'speechiness', 'tempo',
                 'time_signature', 'total_album_tracks', 'track_id', 'genres', 'place_in_album', 'month',
                 'main_genres', 'no_genres'],
        data=[[acousticness, 'album', album_track_no, 'artists', 'artists_id', 'available_markets',
                 'cover_url', danceability, duration_ms, energy, explicit, instrumentalness,
                 liveness, loudness, 'name', 'preview_url', release_date, speechiness, tempo,
                 time_signature, total_album_tracks, 'track_id', 'genres', place_in_album, month,
                 main_genre, no_genres]]
    )

    # loading models
    preprocessor = pickle.load('pickles/fitted_preprocessor.pkl', 'rb'))
    bal_model = pickle.load(open('pickles/balanced_model.pkl', 'rb'))
    strict_model = pickle.load(open('pickles/strict_model.pkl', 'rb'))

    # running models
    df_preprocessed = preprocessor.transform(df)
    y_pred_bal = bal_model.predict(df_preprocessed)
    y_pred_strict = strict_model.predict(df_preprocessed)

    # evaluating model results
    if y_pred_strict == 1:
        pred_pop = f'Congratulations! Your track will become the next big thing! Way to go, superstar!'
    elif y_pred_strict == 0 and y_pred_bal == 1:
        pred_pop= f"It won't be the next 'despacito' but there surely is an audience for your track."
    elif y_pred_strict == 0 and y_pred_bal == 0:
        pred_pop= f'Awww... sorry this track will be no hit!'


    # clusters
    # loading model
    kmeans = pickle.load(open('pickles/kmeans_pipe.pkl', 'rb'))

    # putting the inputted data in the model format
    kmeans_features = df[['acousticness', 'danceability', 'duration_ms', 'energy', 'explicit',
                         'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo',
                         'time_signature', 'main_genres']]

    # running the model
    cluster_pred = kmeans.predict(kmeans_features)

    # finding a sample of 10 instances with the same cluster
    indices = cluster_database[cluster_database['clusters'] == cluster_pred[0]].sample(10).index

    # creating table with these 10 instances for output
    similar = pd.DataFrame(columns=cluster_columns)
    for idx in list(indices):
        name = cluster_database['name'][idx]
        artists = cluster_database['artists'][idx]
        preview = cluster_database['preview_url'][idx]
        cover = cluster_database['cover_url'][idx]
        temp = pd.DataFrame([[name, artists, cover, preview]], columns=cluster_columns)
        similar = pd.concat([similar, temp], axis=0)

    #exporting results to be used in different tab
    pickle.dump(pred_pop, open('temp/pred_pop.pkl','wb'))
    similar.to_pickle('temp/similar.pkl')

    # output
    test =pred_pop
    print(pred_pop)

    return test



