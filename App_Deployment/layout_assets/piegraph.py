#--------------------- Packages
import numpy as np
import pandas as pd
import plotly.graph_objects as go

#--------------------- Sentiment Piegraph
def piegraph_asset(df):
    """Function which returns the pie graphs used for sentiment classification in the twitter feed."""
    fig = go.Figure(data = [
        go.Pie(
            labels = list(df.keys()), values = list(df.values()),
            textinfo = 'label+percent', insidetextorientation = 'radial'
        )
    ])
    
    fig.update_layout(paper_bgcolor = '#eaeaea', height = 550,
                      width = 550, font_size = 20,
                      uniformtext_minsize = 20, uniformtext_mode = 'hide',
                      hoverlabel = dict(font_size = 24)
                     )
    return fig