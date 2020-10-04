#--------------------- Packages
import numpy as np
import pandas as pd
import plotly.graph_objects as go

#--------------------- Sentiment Distribution
def histogram_asset(df):
    """Function which returns a distribution of sentiment classes"""
    colors = ["#a6f1a6", "#e0e0e0", "#ff0000"]
    fig = go.Figure(data=[
        go.Histogram(x = df, marker_color = colors)
    ])
    
    fig.update_xaxes(linewidth = 1, linecolor = 'black', 
                     gridcolor = 'LightPink', automargin = True,  
                     ticks = "outside", tickwidth = 2,
                     tickcolor = 'black', ticklen = 12,
                     title = 'Sentiment', title_font = dict(size = 22))
    
    fig.update_yaxes(linewidth = 1, linecolor = 'black', 
                     gridcolor = 'LightPink', ticks = "outside",
                     tickwidth = 2, tickcolor = 'black',
                     ticklen = 12, title = 'Frequency',
                     title_font = dict(size = 22),
                    )
    
    fig.update_layout(
        font = dict(size = 18),
        legend = dict(
            x = 1,
            y = 1,
            traceorder = "normal",
            font = dict(
                family = "sans-serif",
                size = 18,
                color = "black"
            ),
            bgcolor = "#f7f7f7",
            bordercolor = "#f7f7f7",
            borderwidth = 1
        ),
        plot_bgcolor = "#f7f7f7", paper_bgcolor = "#f7f7f7",
        width = 900, height = 600, 
        hoverlabel = dict(
            font_size = 24, 
            font_family = "Rockwell"),
        xaxis = {'categoryorder':'category descending'}
    )
    return fig