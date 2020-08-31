# importing relevant packages
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import pandas as pd
import base64
from io import BytesIO
from wordcloud import WordCloud
from collections import Counter
import os, inspect

# importing linked files
from app import app

# loading data for graph
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)

data_genre = pd.read_csv(str(parentdir)+'/data/data_w_genres.csv')
data = pd.read_csv(str(parentdir)+'/data/data.csv')
df=data.copy()

# merging the two datasets
df['genre_artist']=df['artists'].str.strip("[]").str.split("',", expand=True)[0].str.strip("'")
df = pd.merge(df,
             data_genre[['artists', 'genres']],
             how='left',
             left_on='genre_artist',
             right_on='artists')
df.rename(columns={'artists_x': 'artists'}, inplace=True)


# page set up
style = {'padding': '1.5em'}

layout = html.Div([
    html.Div([
        dcc.Markdown("### A Century in Music"),
        dcc.Markdown("""The word cloud below shows music of the past century based on release dates.
        Choose whether you would like to see genres or artists and use the slider to adjust the time frame.
        """),
        dcc.Markdown("""Please note that this graph might take some time to load.""")
    ],
        style=style),
    html.Div(
        dcc.RadioItems(
            id='artists_genres',
            options=[
                {'label': 'Artists', 'value': 'artists'},
                {'label': 'Genres', 'value': 'genres'},
            ],
            value='artists',
            labelStyle={'display': 'inline-block'}
        ),
        style={'textAlign': 'center',
               'marginTop': '1.5em'},
    ),

    html.Div([
        html.Img(
            id='wordcloud',
            ),
        dcc.RangeSlider(
            id='year-slider',
            min=1920,
            max=df['year'].max(),
            value=[1920, df['year'].max()],
            marks={str(year): str(year) for year in np.append(df['year'].unique(), [1920]) if year % 10 == 0},
            step=1,
            vertical=False,
            ),
    ],
        style={'textAlign': 'center',
                    'marginTop': '1.5em'},
    ),


])

@app.callback(
    Output('wordcloud', 'src'),
    [Input('year-slider', 'value'),
     Input('artists_genres', 'value')])
def update_figure(selected_years, selected_data):

    # filtering according to year
    filtered_df = df[df['year'].between(selected_years[0], selected_years[1])].copy()

    # filtering according to selected data
    filtered_df = filtered_df[selected_data].str.strip("[]").str.split("',", expand=True)

    # creating a dict of frequencies
    dicts = []
    for col in filtered_df:
        try:
            filtered_df[col] = filtered_df[col].str.replace("'", "")
        except:
            pass
        dicts.append(filtered_df[col].value_counts().to_dict())

        c = Counter()
        for d in dicts:
            c.update(d)

    # reducing dict to 50 most fequent words
    c=dict(c.most_common(50))

    # creating wordcloud and saving it as image
    img = BytesIO()
    wc = WordCloud(collocations=False, max_words=50, background_color="#090024ff", width=900, height=500).generate_from_frequencies(c)
    wc.to_image().save(img, format='PNG')
    return 'data:image/png;base64,{}'.format(base64.b64encode(img.getvalue()).decode())

