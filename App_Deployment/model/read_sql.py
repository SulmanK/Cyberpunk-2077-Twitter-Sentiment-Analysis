#--------------------- Packages
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

import numpy as np
import pandas as pd
import psycopg2

#--------------------- Data Gathering
""" Function to read a dataframe to a sql database."""
def read_tweets(df):
    # PostgreSQL
    ## Connect to our database
    DATABASE_URL = 'enter'
    engine = create_engine(DATABASE_URL)
    conn = psycopg2.connect(DATABASE_URL, sslmode = 'require')
    cursor = conn.cursor()
    
    ## Read in SQL database
    df = pd.read_sql('select * from full_tweets', con = conn, index_col = 'index')
    return df