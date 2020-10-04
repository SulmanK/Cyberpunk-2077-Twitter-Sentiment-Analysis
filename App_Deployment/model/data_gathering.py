#--------------------- Packages
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from tweepy import API
from tweepy import OAuthHandler
from tweepy import Stream
from urllib3.exceptions import ProtocolError

import numpy as np
import pandas as pd
import psycopg2
import tweepy

#--------------------- Data Gathering
""" Function to pull the tweets using the twitter API and then storing it into a postgreSQL database."""
def data_gather(consumer_key, consumer_secret, access_key, access_secret):
    # Twitter API credentials
    consumer_key = consumer_key
    consumer_secret = consumer_secret
    access_key = access_key
    access_secret = access_secret

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # Pull tweets from today's date, we'll start with 300 tweets.
    tweets = tweepy.Cursor(api.search, q = ['#Cyberpunk2077'],
                           since = datetime.now().strftime('%Y-%m-%d'), lang = "en",
                           tweet_mode = 'extended').items(330)

    # Store the tweets in a list
    tweet_list = [tweet for tweet in tweets]

    # Create a dataframe to store the contents of the tweets
    tweet_text = []
    for x in tweet_list:
        tweet_text.append(x.full_text)

    df_tweets = pd.DataFrame(data = tweet_text, columns = ['tweet'])


    # PostgreSQL
    ## Connect to our database
    DATABASE_URL = 'enter'
    engine = create_engine(DATABASE_URL)
    conn = psycopg2.connect(DATABASE_URL, sslmode = 'require')
    cursor = conn.cursor()

    ## Drop existing tables with the tweets name
    cursor.execute('DROP TABLE IF EXISTS tweets')
    cursor.execute('DROP TABLE IF EXISTS full_tweets')
    #cursor.execute('DROP TABLE full_tweets')
    conn.commit()

    ## Store all the tweets from our dataframe to our database
    return df_tweets.to_sql('tweets', con = engine)


consumer_key = 'enter'
consumer_secret = 'enter'
access_key = 'enter'
access_secret = 'enter'

write_sql = data_gather(consumer_key, consumer_secret, access_key, access_secret)