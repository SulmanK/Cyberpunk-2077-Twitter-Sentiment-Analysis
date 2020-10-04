#--------------------- Packages
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import numpy as np
import pandas as pd
import psycopg2
#--------------------- Data Gathering
""" Script to pull the tweets from the PostgreSQL database, retrieves the dataframe and initializes various variables for analysis."""

## Pull the data from the database
### Set up the connection
DATABASE_URL = 'enter'
conn = psycopg2.connect(DATABASE_URL, sslmode = 'require')

### Store into our dataframe df
df = pd.read_sql('select * from tweets', con = conn, index_col = 'index')

### Reindex the values (we will use these for our twitter feed)
df_1t = df[0:30].reset_index()
df_2t = df[31:61].reset_index()
df_3t = df[62:92].reset_index()
df_4t = df[93:123].reset_index()
df_5t = df[124:154].reset_index()
df_6t = df[155:185].reset_index()
df_7t = df[186:216].reset_index()
df_8t = df[217:247].reset_index()
df_9t = df[248:278].reset_index()
df_10t = df[279:309].reset_index()

## Dataframe that will contain all the contents and sentiment of the tweets.
total_tweets_df = pd.DataFrame(columns = ['Tweets', 'Sentiment'])

## Vader Sentiment Analyzer
analyser = SentimentIntensityAnalyzer()
