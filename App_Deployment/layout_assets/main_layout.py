#--------------------- Packages
from app import app
from dash.dependencies import Input, Output
from layout_assets.datatable import datatable_asset
from layout_assets.histogram import histogram_asset
from layout_assets.piegraph import piegraph_asset
from layout_assets.wordcloud import wordcloud_asset
from model.data_gathering import write_sql
from model.read_sql import read_tweets 
from model.write_sql import write_tweets 
from model.data_pull import df_1t, df_2t, df_3t, df_4t, df_5t, df_6t, df_7t, df_8t, df_9t, df_10t, total_tweets_df, analyser
from model.get_interval_values import get_value
from model.sentiment_scores import sentiment_analyzer_scores
from model.sentiment_class import sentiment_logic

import dash_html_components as html
import dash_core_components as dcc
import numpy as np
import pandas as pd
import plotly.graph_objects as go

#--------------------- Main Layout
"""Main Page of Web Application"""


# Layout
main_layout = html.Div([
    html.Div([
                html.Div(
                    [
                        
                        # Input Title of Dashboard, Include title and href link
                        html.H2(
                            id = "banner-title",
                            children = [
                                html.A(
                                    "Cyberpunk Twitter Sentiment Analysis",
                                    href = "https://github.com/SulmanK/Cyberpunk-2077-Twitter-Sentiment-Analysis",
                                    style = {"text-decoration": "none", "color": "inherit", 'padding-left': '55rem'},
                                )
                            ] 
                        ), 
                       
                        # Insert Github Logo with href link
                        html.A(
                            [
                                html.Img(src = app.get_asset_url("github_logo.png"))
                            ], href = "https://github.com/SulmanK/Cyberpunk-2077-Twitter-Sentiment-Analysis",
                        ),
                        
                        # Insert Dash logo with href link
                        html.A( 
                            [
                                html.Img(src = app.get_asset_url("dash_banner.png")) 
                            ], href = "https://dash.plotly.com/",
                        ),
                        
                        # Insert Cyberpunk logo with href link
                        html.A( 
                            [
                                html.Img(src = app.get_asset_url("cyberpunk_logo.png")) 
                            ], href = "https://www.cyberpunk.net/us/en/",
                        ), 
                        
                    ], className = "row",
                )
            ], className = "banner"
),


## Insert Project Introduction
        html.Div(
            [
                dcc.Markdown(
                    ''' 
Cyberpunk 2077 is an upcoming action role-playing video game developed by CD Projekt. With such a large social media following, users are voicing their wishes and concerns to CD Projekt. In this project, we will monitor tweets collected and parse through the sentiment of each. More information on the database collection and sentiment analysis tools used assumptions are in the project repository page and notebook.
'''
                )
            ], style = {'padding': '2rem 4rem 2rem 4rem',
                        'border-top': '10px solid #2DDBE8',
                        'border-bottom': '10px solid #2DDBE8',
                        'fontSize' : 28, 'font-family': "Myriad Pro"}
        ),  
    
## Insert Twitter Feed
    html.Div([
        html.H2('Twitter Feed')
    ]),
    
## Storing our interval in this component every 30 seconds it updates.
    html.Div([
        html.Div(id = 'tweets'),
        dcc.Interval(
            id = 'interval-component',
            interval = 30 * 1000, # in milliseconds
            n_intervals = 0,
            max_intervals = 29,
        ),
        html.Div(id='intermediate-value', style={'display': 'none'}),
    ]),


# Insert Exploration Section (Word Cloud and Distribution Plot)
    html.Div([
        html.H2('Exploration')
    ]),
    
    html.Div(id = 'Exploration')
    
 ], style = {'maxWidth': '2000px', 'height': '80vh',
             'minWidth': '1500px', 'padding-left': '20px'
            }   
)




## Callback function for updating the twitter feed cycles using the intervals

@app.callback(Output('tweets', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_tweets_feed(n):
    """Function which is used to update the twitter feed."""
    
    # Retrieve the tweets
    first_tweet = get_value(df_1t, n)
    second_tweet = get_value(df_2t, n) 
    third_tweet = get_value(df_3t, n)
    fourth_tweet = get_value(df_4t, n)
    fifth_tweet = get_value(df_5t, n)
    sixth_tweet = get_value(df_6t, n)
    seventh_tweet = get_value(df_7t, n)
    eighth_tweet = get_value(df_8t, n)
    nineth_tweet = get_value(df_9t, n)
    tenth_tweet = get_value(df_10t, n) 
    
    # Compute the sentiment of each tweet
    sa_first_tweet = sentiment_analyzer_scores(first_tweet)
    sa_second_tweet = sentiment_analyzer_scores(second_tweet)
    sa_third_tweet = sentiment_analyzer_scores(third_tweet)
    sa_fourth_tweet = sentiment_analyzer_scores(fourth_tweet)
    sa_fifth_tweet = sentiment_analyzer_scores(fifth_tweet)
    sa_sixth_tweet = sentiment_analyzer_scores(sixth_tweet)
    sa_seventh_tweet = sentiment_analyzer_scores(seventh_tweet)
    sa_eighth_tweet = sentiment_analyzer_scores(eighth_tweet)
    sa_nineth_tweet = sentiment_analyzer_scores(nineth_tweet)
    sa_tenth_tweet = sentiment_analyzer_scores(tenth_tweet)
    
    # Return the tweet contents and a pie graph of the sentiment.
    
    return html.Div([
        html.Div([

# First Tweet
            html.Div([
                html.Div([
                    html.Pre(str(first_tweet)),
                ], 
                    className = 'ten columns',
                    style = {
                        'backgroundColor': 'white',
                        'box-shadow': '2px 2px 10px #ccc',
                        'padding': '10px',
                        'padding-bottom': '25px',
                        'margin': '30px',
                        'overflowX': 'scroll',
                        'fontSize': '22px',
                    }
                ),
                html.Div([
                    dcc.Graph(figure = piegraph_asset(sa_first_tweet))
                ],
                    className = 'nine columns',
                    style = {"padding-left": "550px", }
                ),
            ], 
                className = 'row' 
            ),
 
# Second Tweet
            
            html.Div([
                html.Div([
                    html.Pre(str(second_tweet)),
                ], 
                    className = 'ten columns',
                    style = {
                        'backgroundColor': 'white',
                        'box-shadow': '3px 3px 10px #ccc',
                        'padding': '10px',
                        'padding-bottom': '25px',
                        'margin': '30px',
                        'overflowX': 'scroll',
                        'fontSize': '22px'}
                ),
                html.Div([
                    dcc.Graph(figure = piegraph_asset(sa_second_tweet))
                ],
                    className = 'nine columns',
                    style = {"padding-left": "550px"}
                ),
            ], 
                className = 'row' 
            ),
        
 # Third Tweet
            
            html.Div([
                html.Div([
                    html.Pre(str(third_tweet)),
                ], 
                    className = 'ten columns',
                    style = {
                        'backgroundColor': 'white',
                        'box-shadow': '3px 3px 10px #ccc',
                        'padding': '10px',
                        'padding-bottom': '25px',
                        'margin': '30px',
                        'overflowX': 'scroll',
                        'fontSize': '22px'}
                ),
                html.Div([
                    dcc.Graph(figure = piegraph_asset(sa_third_tweet))
                ],
                    className = 'nine columns',
                    style = {"padding-left": "550px"}
                ),
            ], 
                className = 'row' 
            ),
        
 # Fourth Tweet
        
        html.Div([
            html.Div([
                html.Pre(str(fourth_tweet)),
            ], 
                className = 'ten columns',
                style = {
                    'backgroundColor': 'white',
                    'box-shadow': '3px 3px 10px #ccc',
                    'padding': '10px',
                    'padding-bottom': '25px',
                    'margin': '30px',
                    'overflowX': 'scroll',
                    'fontSize': '22px'}
            ),
            html.Div([
                dcc.Graph(figure = piegraph_asset(sa_fourth_tweet))
            ],
                className = 'nine columns',
                style = {"padding-left": "550px"}
            ),
        ], 
            className = 'row' 
        ),


 # Fifth Tweet
        
        html.Div([
            html.Div([
                html.Pre(str(fifth_tweet)),
            ], 
                className = 'ten columns',
                style = {
                    'backgroundColor': 'white',
                    'box-shadow': '3px 3px 10px #ccc',
                    'padding': '10px',
                    'padding-bottom': '25px',
                    'margin': '30px',
                    'overflowX': 'scroll',
                    'fontSize': '22px'}
            ),
            html.Div([
                dcc.Graph(figure = piegraph_asset(sa_fifth_tweet))
            ],
                className = 'nine columns',
                style = {"padding-left": "550px"}
            ),
        ], 
            className = 'row' 
        ),
        

 # Sixth Tweet
        html.Div([
            html.Div([
                html.Pre(str(sixth_tweet)),
            ], 
                className = 'ten columns',
                style = {
                    'backgroundColor': 'white',
                    'box-shadow': '3px 3px 10px #ccc',
                    'padding': '10px',
                    'padding-bottom': '25px',
                    'margin': '30px',
                    'overflowX': 'scroll',
                    'fontSize': '22px'}
            ),
            html.Div([
                dcc.Graph(figure = piegraph_asset(sa_sixth_tweet))
            ],
                className = 'nine columns',
                style = {"padding-left": "550px"}
            ),
        ], 
            className = 'row' 
        ),
        
 # Seventh Tweet
        
        html.Div([
            html.Div([
                html.Pre(str(seventh_tweet)),
            ], 
                className = 'ten columns',
                style = {
                'backgroundColor': 'white',
                'box-shadow': '3px 3px 10px #ccc',
                'padding': '10px',
                'padding-bottom': '25px',
                'margin': '30px',
                'overflowX': 'scroll',
                'fontSize': '22px'}
            ),
    
    html.Div([
        dcc.Graph(figure = piegraph_asset(sa_seventh_tweet))
    ],
        className = 'nine columns',
        style = {"padding-left": "550px"}
    ),
        ], 
            className = 'row' 
        ),

 # Eighth Tweet
        
        html.Div([
            html.Div([
                html.Pre(str(eighth_tweet)),
            ], 
                className = 'ten columns',
                style = {
                    'backgroundColor': 'white',
                    'box-shadow': '3px 3px 10px #ccc',
                    'padding': '10px',
                    'padding-bottom': '25px',
                    'margin': '30px',
                    'overflowX': 'scroll',
                    'fontSize': '22px'}
                    ),
    
    html.Div([
        dcc.Graph(figure = piegraph_asset(sa_eighth_tweet))
    ],
        className = 'nine columns',
        style = {"padding-left": "550px"}
    ),
        ], 
            className = 'row' 
        ),

 # Nineth
        
        html.Div([
            html.Div([
                html.Pre(str(nineth_tweet)),
            ], 
                className = 'ten columns',
                style = {
                    'backgroundColor': 'white',
                    'box-shadow': '3px 3px 10px #ccc',
                    'padding': '10px',
                    'padding-bottom': '25px',
                    'margin': '30px',
                    'overflowX': 'scroll',
                    'fontSize': '22px'}
            ),
            html.Div([
                dcc.Graph(figure = piegraph_asset(sa_nineth_tweet))
            ],
                className = 'nine columns',
                style = {"padding-left": "550px"}
            ),
        ], 
            className = 'row' 
        ),

 # Tenth Tweet
        
        html.Div([
            html.Div([
                html.Pre(str(tenth_tweet)),
            ], 
                className = 'ten columns',
                style = {
                    'backgroundColor': 'white',
                    'box-shadow': '3px 3px 10px #ccc',
                    'padding': '10px',
                    'padding-bottom': '25px',
                    'margin': '30px',
                    'overflowX': 'scroll',
                    'fontSize': '22px'}
            ),
            html.Div([
                dcc.Graph(figure = piegraph_asset(sa_tenth_tweet))
            ],
                className = 'nine columns',
                style = {"padding-left": "550px"}
            ),
        ], 
            className = 'row' 
        ),
        ], style = {'overflowY': 'scroll', 'overflowX': 'hidden',
                    'maxHeight': '105ex', 'backgroundColor' : '#eaeaea'}
    ),
    
    ])

# Dataframe callback
@app.callback(Output('intermediate-value', 'children'),
              [Input('interval-component', 'n_intervals')])

def tweet_df(n):
    """Function which returns the all the tweets stored in the dataframe"""
    # Retrieve the tweet contents
    first_tweet = get_value(df_1t, n)
    second_tweet = get_value(df_2t, n) 
    third_tweet = get_value(df_3t, n)
    fourth_tweet = get_value(df_4t, n)
    fifth_tweet = get_value(df_5t, n)
    sixth_tweet = get_value(df_6t, n)
    seventh_tweet = get_value(df_7t, n)
    eighth_tweet = get_value(df_8t, n)
    nineth_tweet = get_value(df_9t, n)
    tenth_tweet = get_value(df_10t, n) 
    
    # Sentiment of each tweet
    sa_first_tweet = sentiment_analyzer_scores(first_tweet)
    sa_second_tweet = sentiment_analyzer_scores(second_tweet)
    sa_third_tweet = sentiment_analyzer_scores(third_tweet)
    sa_fourth_tweet = sentiment_analyzer_scores(fourth_tweet)
    sa_fifth_tweet = sentiment_analyzer_scores(fifth_tweet)
    sa_sixth_tweet = sentiment_analyzer_scores(sixth_tweet)
    sa_seventh_tweet = sentiment_analyzer_scores(seventh_tweet)
    sa_eighth_tweet = sentiment_analyzer_scores(eighth_tweet)
    sa_nineth_tweet = sentiment_analyzer_scores(nineth_tweet)
    sa_tenth_tweet = sentiment_analyzer_scores(tenth_tweet)
    
    # Compute the compound score for obtaining a sentiment class
    compound_score_first_tweet = sentiment_logic((list(sa_first_tweet.values())[list(sa_first_tweet.keys()).index('compound')] ))
    compound_score_second_tweet = sentiment_logic((list(sa_second_tweet.values())[list(sa_second_tweet.keys()).index('compound')] )) 
    compound_score_third_tweet = sentiment_logic((list(sa_third_tweet.values())[list(sa_third_tweet.keys()).index('compound')] ))
    compound_score_fourth_tweet = sentiment_logic((list(sa_fourth_tweet.values())[list(sa_fourth_tweet.keys()).index('compound')] ))
    compound_score_fifth_tweet = sentiment_logic((list(sa_fifth_tweet.values())[list(sa_fifth_tweet.keys()).index('compound')] ))
    compound_score_sixth_tweet = sentiment_logic((list(sa_sixth_tweet.values())[list(sa_sixth_tweet.keys()).index('compound')] ))
    compound_score_seventh_tweet = sentiment_logic((list(sa_seventh_tweet.values())[list(sa_seventh_tweet.keys()).index('compound')] ))
    compound_score_eighth_tweet = sentiment_logic((list(sa_eighth_tweet.values())[list(sa_eighth_tweet.keys()).index('compound')] ))
    compound_score_nineth_tweet = sentiment_logic((list(sa_nineth_tweet.values())[list(sa_nineth_tweet.keys()).index('compound')] ))
    compound_score_tenth_tweet = sentiment_logic((list(sa_tenth_tweet.values())[list(sa_tenth_tweet.keys()).index('compound')] ))
    
    # Create a new temporary dataframe for the tweet contents and sentiment
    compound_score_list = [compound_score_first_tweet, compound_score_second_tweet,
                           compound_score_third_tweet, compound_score_fourth_tweet,
                           compound_score_fifth_tweet, compound_score_sixth_tweet, 
                           compound_score_seventh_tweet, compound_score_eighth_tweet,
                           compound_score_nineth_tweet, compound_score_tenth_tweet]
    
    
    first_col = [first_tweet, second_tweet,
              third_tweet, fourth_tweet,
              fifth_tweet, sixth_tweet,
              seventh_tweet, eighth_tweet,
              nineth_tweet, tenth_tweet]
    
    second_col = compound_score_list
    
    tmp_df = pd.DataFrame(data = {'Tweets' : first_col, 
                                 'Sentiment' : second_col})
   
    
    return tmp_df.to_json(date_format = 'iso', orient = 'split')


# Exploration callback functions
@app.callback(Output('Exploration', 'children'),
              [Input('intermediate-value', 'children')])

def exploration(tmp_df):
    "Function which returns the contents of the exploration section - wordcloud and sentiment distribution" 
    # Read in intermediate value container
    df = pd.read_json(tmp_df, orient='split')
    
    # Write it to database
    write_tweets(df)
    
    # Read in the full dataframe
    total_tweets_df = read_tweets(df)
    
    # Extract the contents of the tweets for the wordcloud
    full_string = ''
    for x in total_tweets_df['Tweets']:
        full_string += x
    
    wc = wordcloud_asset(full_string)
    
    # Initialize datatable
    datatable = datatable_asset(df = total_tweets_df)
    
    # Initialize histogram
    histogram = histogram_asset(total_tweets_df['Sentiment'])
    
    return html.Div([
        # Datatable
        html.Div([
            datatable
        ], className = 'row'
        ),
       # Wordcloud and Distribution
        html.Div([
            html.Div([
                html.Img(src="data:image/png;base64," + wc)
            ],
                className = 'one-half column'
            ),
            html.Div([
                dcc.Graph(figure = histogram)
            ],
                className = 'one-half column')             
        ],
            className = 'row'
        )
    ])