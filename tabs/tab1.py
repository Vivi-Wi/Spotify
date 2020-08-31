# importing relevant packages
import dash_core_components as dcc
import dash_html_components as html

# introducing the project

# page set up
layout = [
    html.Div(html.Img(src='https://www.alizila.com/wp-content/uploads/2019/07/audio-graphic-headphones-music-streaming-992x523.png',
                      style={'height' : '90%',
                          'width':'90%'}),
             style={'textAlign': 'center',
                    'marginTop': '1.5em'}),
    dcc.Markdown("""
          ### Intro
          The times of video killed the radio star are clearly over but what is it that makes stars nowadays? 
          Attempting to find an answer to this question I have looked at Spotify data from the past 100 years and more
          specifically tracks from 2019. 
          Using machine learning algorithms popularity was predicted both continuously and in binary classes. 
          Finally, clustering was used to find similarities that could be used in a recommender system.
          The entire analysis and models tested can be viewed here: https://github.com/Vivi-Wi/Spotify
          
          The most accurate model and the model that is most securely predicts hits form the basis for the tool used in this app.
          About 348k tracks, that were released 2019 and retrieved via the Spotify API are used as a database for comparison.
          """
                 )
]
