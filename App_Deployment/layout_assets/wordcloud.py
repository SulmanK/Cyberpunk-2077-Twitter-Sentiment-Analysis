#--------------------- Packages
from io import BytesIO
from wordcloud import WordCloud

import base64
import numpy as np
import pandas as pd

#--------------------- WordCloud
def wordcloud_asset(text):
    """Function to create and plot a worcloud"""

    # The regex expression is used to eliminate all non english letters
    regex_expression = r"[a-zA-Z]+"
    
    # Word Cloud
    wc = WordCloud(width = 800, height = 600, max_words = 10000, 
                      relative_scaling = 0, background_color = '#f7f7f7', contour_color = "black",
                      regexp = regex_expression, random_state = 2, colormap = 'gnuplot2',
                      collocations = False,
             ).generate(text)
    
    wc_img = wc.to_image()
    with BytesIO() as buffer:
        wc_img.save(buffer, 'png')
        final_img = base64.b64encode(buffer.getvalue()).decode()
    
    return final_img