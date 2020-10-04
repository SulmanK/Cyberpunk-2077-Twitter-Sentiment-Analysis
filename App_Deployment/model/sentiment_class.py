#--------------------- Packages
import pandas as pd

#--------------------- Sentiment class
def sentiment_logic(text):
    """Function which outputs the sentiment class."""
    if text >= 0.05:
        result = 'Positive'
    elif (text > -0.05) & (text < 0.05):
        result = 'Neutral'
    elif text <= -0.05:
        result = 'Negative'
    return result