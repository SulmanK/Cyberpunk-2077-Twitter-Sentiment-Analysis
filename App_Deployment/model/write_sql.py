#--------------------- Packages
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

import numpy as np
import pandas as pd
import psycopg2

#--------------------- Data Gathering
""" Function to write a dataframe to a sql database."""
def write_tweets(df):
    # PostgreSQL
    ## Connect to our database
    DATABASE_URL = 'enter'
    engine = create_engine(DATABASE_URL)
    conn = psycopg2.connect(DATABASE_URL, sslmode = 'require')
    cursor = conn.cursor()


    ## Store all the tweets from our dataframe to our database
    return df.to_sql('full_tweets', con = engine, if_exists='append')