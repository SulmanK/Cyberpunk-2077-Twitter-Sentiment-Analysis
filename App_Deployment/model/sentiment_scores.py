#--------------------- Packages
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import pandas as pd

#--------------------- Sentiment Scores
def sentiment_analyzer_scores(sentence):
    """Function which returns the sentiment polarity score from VADER"""
    analyser = SentimentIntensityAnalyzer()
    score = analyser.polarity_scores(sentence)
    return score